from fastapi import Depends, FastAPI
from fastapi import APIRouter
from sqlalchemy.orm import Session
from services.genre import read_all_genre, read_genre_by_id, read_genre_by_name, create_genre, update_genre, delete_genre
from core.database import get_db
from schemas.genre import GenreCreate, GenreUpdate, GenreRead
from typing import List

router = APIRouter()

# READ 
@router.get("/{id}", response_model=GenreRead)
def genre_read_by_id(id: int, db: Session = Depends(get_db)):
    return read_genre_by_id(db, id)

@router.get("/{name}", response_model=GenreRead)
def work_read_by_name(name: str, db: Session = Depends(get_db)):
    return read_genre_by_name(db, name)

@router.get("/", response_model=List[GenreRead])
def genre_read_all(db: Session = Depends(get_db)):
    return read_all_genre(db)

# CREATE
@router.post("/", response_model=GenreRead)
def genre_create(genre: GenreCreate, db: Session = Depends(get_db)):
    return create_genre(db, genre)

# UPDATE
@router.patch("/{id}", response_model=GenreRead)
def genre_update(id: int, data: GenreUpdate, db: Session = Depends(get_db)):
    return update_genre(db, id, data)

# DELETE
@router.delete("/{id}", response_model = GenreRead)
def genre_delete(id: int, db: Session = Depends(get_db)):
    return delete_genre(db, id)
