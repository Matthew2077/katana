from pydantic import BaseModel, ConfigDict
from typing import Optional


class MangaBase(BaseModel):
    name: str
    genre_id: int
    season: int
    total_chapters: int
    watched_chapters: int
    model_config = ConfigDict(from_attributes=True)

class MangaCreate(MangaBase):
    pass

class MangaUpdate(BaseModel):
    name: Optional[str] = None
    genre_id: Optional[int] = None
    season: Optional[int] = None
    total_chapters: Optional[int] = None
    watched_chapters: Optional[int] = None
    model_config = ConfigDict(from_attributes=True)

class NovelRead(MangaBase):
    id: int
