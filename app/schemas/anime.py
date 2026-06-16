from pydantic import BaseModel, ConfigDict
from typing import Optional


class AnimeBase(BaseModel):
    name: str
    genre_id: int
    season: int
    total_episodes: int
    watched_episodes: int
    model_config = ConfigDict(from_attributes=True)

class AnimeCreate(AnimeBase):
    pass

class AnimeUpdate(BaseModel):
    name: Optional[str] = None
    genre_id: Optional[int] = None
    season: Optional[int] = None
    total_episodes: Optional[int] = None
    watched_episodes: Optional[int] = None
    model_config = ConfigDict(from_attributes=True)

class AnimeRead(AnimeBase):
    id: int
