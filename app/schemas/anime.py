from pydantic import BaseModel, ConfigDict
from typing import Optional

class AnimeBase(BaseModel):
    id: int
    name: str
    season: int
    episodes_total: int
    episodes_watched: int
    genre_id: int
    model_config = ConfigDict(from_attributes=True)


class AnimeCreate(AnimeBase):
    pass

class AnimeUpdate(BaseModel):
    id: Optional[int] = None
    name: Optional[str] = None
    season: Optional[int] = None
    episodes_total: Optional[int] = None
    episodes_watched: Optional[int] = None
    genre_id: Optional[int] = None
    model_config = ConfigDict(from_attributes=True)

class AnimeRead(AnimeBase):
    pass


