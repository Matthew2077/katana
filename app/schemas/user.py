from pydantic import BaseModel, ConfigDict
from typing import Optional

# USER ----------
class UserBase(BaseModel):
    id: int
    name: str
    model_config = ConfigDict(from_attributes=True)

class UserCreate(UserBase):
    pass

class UserUpdate(BaseModel):
    id: Optional[int] = None
    name: Optional[str] = None
    model_config = ConfigDict(from_attributes=True)

class UserRead(UserBase):
    pass


# ADMIN -------
class AdminBase(BaseModel):
    id: int
    name: str
    role: str
    department: str
    model_config = ConfigDict(from_attributes=True)

class AdminCreate(AdminBase):
    pass

class AdminUpdate(BaseModel):
    id: Optional[int] = None
    name: Optional[str] = None
    role: Optional[str] = None
    department: Optional[str] = None
    model_config = ConfigDict(from_attributes=True)


class AdminRead(AdminBase):
    pass