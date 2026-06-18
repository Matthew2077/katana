from fastapi import Depends, FastAPI
from fastapi import APIRouter
from sqlalchemy.orm import Session
from services.user import read_all_users, read_user_by_name, read_user_by_id, create_user, update_user, delete_user
from core.database import get_db
from schemas.user import UserCreate, UserRead, UserUpdate
from typing import List

router = APIRouter()


# READ 
@router.get("/{id}", response_model=UserRead)
def user_read_by_id(id: int, db: Session = Depends(get_db)):
    return read_user_by_id(db, id)

@router.get("/{name}", response_model=UserRead)
def user_read_by_name(name: str, db: Session = Depends(get_db)):
    return read_user_by_name(db, name)

@router.get("/", response_model=List[UserRead])
def user_read_all(db: Session = Depends(get_db)):
    return read_all_users(db)

# CREATE
@router.post("/", response_model=UserRead)
def user_create(user: UserCreate, db: Session = Depends(get_db)):
    return create_user(db, user)

# UPDATE
@router.patch("/{id}", response_model=UserRead)
def user_update(id: int, data: UserUpdate, db: Session = Depends(get_db)):
    return update_user(db, id, data)

# DELETE
@router.delete("/{id}", response_model = UserRead)
def user_delete(id: int, db: Session = Depends(get_db)):
    return delete_user(db, id)
