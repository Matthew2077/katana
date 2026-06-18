from fastapi import Depends, FastAPI
from fastapi import APIRouter
from sqlalchemy.orm import Session
from services.anime import read_anime_by_id, read_anime_by_name, read_all_anime, create_anime, update_anime, delete_anime
from core.database import get_db
from schemas.anime import AnimeCreate, AnimeUpdate, AnimeRead
from typing import List

router = APIRouter()

# READ 
@router.get("/{id}", response_model=AnimeRead)
def anime_read_by_id(id: int, db: Session = Depends(get_db)):
    return anime_read_by_id(db, id)

@router.get("/{name}", response_model=AnimeRead)
def work_read_by_name(name: str, db: Session = Depends(get_db)):
    return read_anime_by_name(db, name)

@router.get("/", response_model=List[AnimeRead])
def anime_read_all(db: Session = Depends(get_db)):
    return read_all_anime(db)

# CREATE
@router.post("/", response_model=AnimeRead)
def anime_create(anime: AnimeCreate, db: Session = Depends(get_db)):
    return create_anime(db, anime)

# UPDATE
@router.patch("/{id}", response_model=AnimeRead)
def anime_update(id: int, data: AnimeUpdate, db: Session = Depends(get_db)):
    return update_anime(db, id, data)

# DELETE
@router.delete("/{id}", response_model = AnimeRead)
def anime_delete(id: int, db: Session = Depends(get_db)):
    return delete_anime(db, id)
