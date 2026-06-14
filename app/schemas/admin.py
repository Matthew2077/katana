from pydantic import BaseModel, ConfigDict
from typing import Optional


class AdminBase(BaseModel):
    name: str
    rank: str
    department: str
    model_config = ConfigDict(from_attributes=True)

class AdminCreate(AdminBase):
    pass

class AdminUpdate(BaseModel):
    name: Optional[str] = None
    rank: Optional[str] = None
    department: Optional[str] = None
    model_config = ConfigDict(from_attributes=True)


class AdminRead(AdminBase):
    id: Optional[int] = None


