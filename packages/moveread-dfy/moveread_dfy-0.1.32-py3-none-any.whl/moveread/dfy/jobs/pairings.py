from typing import Sequence, Callable, Awaitable, Unpack
from datetime import datetime, timedelta
from sqlmodel import select, Session
from haskellian import iter as I
import chess_pairings as cp
import chess_scraping as cs
from moveread.dfy import Group, Round, Pairings, Game, Tournament, queries
from haskellian import Either, Left, Right
from dslog import Logger

def current_pairings(session: Session, now: datetime | None = None):
  now = now or datetime.now()
  tomorrow = now + timedelta(days=1)
  yesterday = now - timedelta(days=1)
  stmt = select(Tournament, Pairings) \
    .where(Tournament.start_date < tomorrow, yesterday < Tournament.end_date) \
    .join(Pairings, Tournament.tournId == Pairings.tournId) # type: ignore
  return session.exec(stmt).all()

def paired_round(session: Session, **roundId: Unpack[cp.RoundId]):
  """Does the round have pairings?"""
  stmt = queries.select_round_games(**roundId)
  return session.exec(stmt).first() is not None

def finished_round(session: Session, **roundId: Unpack[cp.RoundId]):
  """Does the round have all results? (WARNING: will return true if unpaired! - by vacuity)"""
  stmt = queries.select_round_games(**roundId).where(Game.result == None)
  return session.exec(stmt).first() is None

def current_round(
  session: Session, tournId: str, group: str, *, now: datetime | None = None,
  paired_round = paired_round, finished_round = finished_round
):
  """Determine the current round, whose pairings should be polled"""
  now = now or datetime.now()
  if not (rounds := session.exec(queries.select_rounds(tournId, group)).all()):
    return Left(f'No rounds found for group "{tournId}/{group}"')
  
  if (prev := I.find_last_idx(lambda r: r.start_dtime < now, rounds)) is None:
    return Right(rounds[0].name)
  
  # if next round (which hasn't yet started) is paired, nothing to do
  if paired_round(session, **cp.roundId(tournId, group, rounds[prev+1].name)):
    return Right(None)
  
  # if current round is finished, poll the next round
  if finished_round(session, **cp.roundId(tournId, group, rounds[prev].name)):
    return Right(rounds[prev+1].name)
  
  # otherwise, poll the current round
  return Right(rounds[prev].name)

def update_rounds(session: Session, tnmt: Tournament, group: str, rounds: Sequence[str]) -> Either[str, str]:
  """Update the group's `rounds` list"""
  grp = session.get(Group, (tnmt.tournId, group))
  if grp is None:
    return Left(f'Group "{tnmt.tournId}/{group}" not found')
  elif grp.rounds != rounds:
    og_rounds = [*grp.rounds]
    grp.rounds = rounds
    session.add(grp)
    session.commit()
    return Right(f'Updated group "{tnmt.tournId}/{group}". Rounds {og_rounds} -> {rounds}')
  else:
    return Right(f'Group "{tnmt.tournId}/{group}" already has rounds {rounds}')
  
def update_round_pairings(session: Session, *, tournId: str, group: str, round: str, pairings: cp.RoundPairings):
  """Insert/update pairings of a round"""
  round_games = session.exec(queries.select_round_games(**cp.roundId(tournId, group, round))).all()
  games_idx = cp.GamesMapping[Game].from_pairs([(g.gameId(), g) for g in round_games])
  added: list[cp.GameId] = []
  updated: list[cp.GameId] = []

  for board, pair in pairings.items():
    if pair.tag != 'paired':
      continue
    gid = cp.gameId(tournId, group, round, board)
    if gid in games_idx:
      game = games_idx[gid]
      if game.white != pair.white or game.black != pair.black or game.result != pair.result:
        game.white = pair.white; game.black = pair.black; game.result = pair.result
        updated.append(gid)
    else:
      game = Game(
        tournId=tournId, group=group, round=round, board=board, index=int(board)-1,
        white=pair.white, black=pair.black, result=pair.result
      )
      added.append(gid)
    session.add(game)
  
  session.commit()
  return added, updated
    
  
def update_group_pairings(session: Session, *, tournId: str, group: str, pairings: cp.GroupPairings):
    """Insert/update pairings of a group"""
    group_games = session.exec(queries.select_group_games(tournId, group)).all()
    games_idx = cp.GamesMapping[Game].from_pairs([(g.gameId(), g) for g in group_games])
    added: list[cp.GameId] = []
    updated: list[cp.GameId] = []

    for round, rnd_pairings in pairings.items():
      for board, pair in rnd_pairings.items():
        if pair.tag != 'paired':
          continue
        gid = cp.gameId(tournId, group, round, board)
        if gid in games_idx:
          game = games_idx[gid]
          if game.white != pair.white or game.black != pair.black or game.result != pair.result:
            game.white = pair.white; game.black = pair.black; game.result = pair.result
            updated.append(gid)
        else:
          game = Game(
            tournId=tournId, group=group, round=round, board=board, index=int(board)-1,
            white=pair.white, black=pair.black, result=pair.result
          )
          added.append(gid)
        
        session.add(game)
    
    session.commit()
    return added, updated


async def scrape_all_pairings(
  session: Session, *, now: datetime | None = None, logger: Logger = Logger.click(),
  scrape_group: Callable[[cs.Source], Awaitable[Either[cs.ScrapingError, cp.GroupPairings]]] = cs.scrape_group
):
  """Updates pairings for all ongoing tournaments"""
  pairing_sources = current_pairings(session, now)
  current_tnmts = [tnmt.tournId for tnmt, _ in pairing_sources]
  logger(f'Updating current tournaments: {", ".join(current_tnmts)}')
  for tnmt, src in pairing_sources:
    e = await scrape_group(src.pairings)
    if e.tag == 'left':
      logger(f'Error fetching pairings for "{tnmt.tournId}/{src.group}"', e.value, level='ERROR')
      continue
    pairings = e.value
    rounds = [str(i+1) for i in range(len(pairings))]
    r = update_rounds(session, tnmt, src.group, rounds)
    logger(r.value, level='DEBUG' if r.tag == 'right' else 'ERROR')
    added, updated = update_group_pairings(session, tournId=tnmt.tournId, group=src.group, pairings=pairings)
    logger(f'Updated pairings for "{tnmt.tournId}/{src.group}", added {len(added)} and updated {len(updated)} games', level='DEBUG')