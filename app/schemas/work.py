from pydantic import BaseModel, ConfigDict
from typing import Optional

class WorkBase(BaseModel):
    name: str
    genre_id: int
    model_config = ConfigDict(from_attributes=True)

class WorkCreate(WorkBase):
    pass

class WorkUpdate(BaseModel):
    id: Optional[int] = None
    name: Optional[str] = None
    genre_id: Optional[int] = None
    model_config = ConfigDict(from_attributes=True)

class WorkRead(WorkBase):
    id: int
