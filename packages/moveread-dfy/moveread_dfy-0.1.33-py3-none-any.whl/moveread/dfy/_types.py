from typing import Sequence, ClassVar, Literal
from dataclasses import dataclass
from datetime import date, datetime
from sqlmodel import Field, SQLModel, Relationship
from sqltypes import SpaceDelimitedList, ValidatedStr, ValidatedJSON
from chess_pairings import GameId, gameId, Result
from chess_scraping import Source

class SheetModel(SQLModel, table=True):
  tournId: str = Field(primary_key=True, foreign_key='tournament.tournId')
  model: str

class Tournament(SQLModel, table=True):
  tournId: str = Field(primary_key=True)
  name: str
  site: str | None = None
  start_date: date
  end_date: date
  groups: Sequence[str] = Field(sa_type=SpaceDelimitedList)

class Pairings(SQLModel, table=True):
  tournId: str = Field(foreign_key='tournament.tournId', primary_key=True)
  group: str = Field(primary_key=True)
  pairings: Source = Field(sa_type=ValidatedJSON(Source))

class Group(SQLModel, table=True):
  tournId: str = Field(primary_key=True, foreign_key='tournament.tournId')
  name: str = Field(primary_key=True)
  rounds: Sequence[str] = Field(sa_type=SpaceDelimitedList)

class Round(SQLModel, table=True):
  tournId: str = Field(primary_key=True, foreign_key='tournament.tournId')
  group: str = Field(primary_key=True)
  name: str = Field(primary_key=True)
  start_dtime: datetime
  
class Image(SQLModel, table=True):
  id: int | None = Field(default=None, primary_key=True)
  url: str
  descaled_url: str
  gameId: int = Field(default=None, foreign_key='game.id')

class FrontendPGN(SQLModel):
  moves: Sequence[str] = Field(sa_type=SpaceDelimitedList)
  early: bool | None = None

class PGN(FrontendPGN, table=True):
  gameId: int = Field(default=None, primary_key=True, foreign_key='game.id')

@dataclass
class Paired:
  white: str
  black: str
  result: Result | None = None
  tag: Literal['paired'] = 'paired'

@dataclass
class FrontendGame:
  board: str
  pairing: Paired
  status: 'Game.Status | None' = None

  @classmethod
  def of(cls, game: 'Game'):
    return cls(game.board, Paired(white=game.white, black=game.black, result=game.result), game.status)

class Game(SQLModel, table=True):
  Status: ClassVar = Literal['uploaded', 'doing', 'done']
  status: 'Game.Status | None' = Field(default=None, sa_type=ValidatedStr(Status))
  id: int | None = Field(default=None, primary_key=True)
  tournId: str = Field(foreign_key='tournament.tournId')
  group: str
  round: str
  board: str
  index: int
  """Boards may have out of whack names (e.g. in team tournaments "1.3"). This is the order you'd see in chess-results"""
  white: str
  black: str
  result: Result | None = Field(sa_type=ValidatedStr(Result))
  imgs: list[Image] = Relationship()
  pgn: PGN | None = Relationship()

  def gameId(self) -> GameId:
    return gameId(self.tournId, self.group, self.round, self.board)
  
class Token(SQLModel, table=True):
  id: int | None = Field(default=None, primary_key=True)
  token: str
  tournId: str = Field(foreign_key='tournament.tournId')
  
__all__ = [
  'Game', 'GameId', 'Image', 'Tournament', 'PGN', 'Paired', 'Token'
]