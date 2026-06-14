from pydantic import BaseModel, ConfigDict
from typing import Optional

class NovelBase(BaseModel):
    name: str
    genre_id: int
    season: int
    total_pages: int
    watched_pages: int
    model_config = ConfigDict(from_attributes=True)

class NovelCreate(NovelBase):
    pass

class NovelUpdate(BaseModel):
    name: Optional[str] = None
    genre_id: Optional[int] = None
    season: Optional[int] = None
    total_pages: Optional[int] = None
    watched_pages: Optional[int] = None
    model_config = ConfigDict(from_attributes=True)

class NovelRead(NovelBase):
    id: int
