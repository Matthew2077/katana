from fastapi import Depends, FastAPI
from fastapi import APIRouter
from sqlalchemy.orm import Session
from services.manga import read_manga_by_id, read_manga_by_name, read_all_manga, create_manga, update_manga, delete_manga
from core.database import get_db
from schemas.manga import MangaCreate, MangaUpdate, MangaRead
from typing import List

router = APIRouter()

# READ 
@router.get("/{id}", response_model=MangaRead)
def manga_read_by_id(id: int, db: Session = Depends(get_db)):
    return read_manga_by_id(db, id)

@router.get("/{name}", response_model=MangaRead)
def work_read_by_name(name: str, db: Session = Depends(get_db)):
    return read_manga_by_name(db, name)

@router.get("/", response_model=List[MangaRead])
def manga_read_all(db: Session = Depends(get_db)):
    return read_all_manga(db)

# CREATE
@router.post("/", response_model=MangaRead)
def manga_create(manga: MangaCreate, db: Session = Depends(get_db)):
    return create_manga(db, manga)

# UPDATE
@router.patch("/{id}", response_model=MangaRead)
def manga_update(id: int, data: MangaUpdate, db: Session = Depends(get_db)):
    return update_manga(db, id, data)

# DELETE
@router.delete("/{id}", response_model = MangaRead)
def manga_delete(id: int, db: Session = Depends(get_db)):
    return delete_manga(db, id)

