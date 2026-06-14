from pydantic import BaseModel, ConfigDict
from typing import Optional

class GenreBase(BaseModel):
    name: str
    label: str
    model_config = ConfigDict(from_attributes=True)

class GenreCreate(GenreBase):
    pass

class GenreUpdate(BaseModel):
    name: Optional[str] = None
    label: Optional[str] = None
    model_config = ConfigDict(from_attributes=True)

class GenreRead(GenreBase):
    id: int