from fastapi import Depends, FastAPI
from fastapi import APIRouter
from sqlalchemy.orm import Session
from services.novel import read_novel_by_id, read_novel_by_name, read_all_novel, create_novel, update_novel, delete_novel
from core.database import get_db
from schemas.novel import NovelRead, NovelUpdate, NovelCreate
from typing import List

router = APIRouter()

# READ 
@router.get("/{id}", response_model=NovelRead)
def novel_read_by_id(id: int, db: Session = Depends(get_db)):
    return novel_read_by_id(db, id)

@router.get("/{name}", response_model=NovelRead)
def work_read_by_name(name: str, db: Session = Depends(get_db)):
    return read_novel_by_name(db, name)

@router.get("/", response_model=List[NovelRead])
def novel_read_all(db: Session = Depends(get_db)):
    return read_all_novel(db)

# CREATE
@router.post("/", response_model=NovelRead)
def novel_create(novel: NovelCreate, db: Session = Depends(get_db)):
    return create_novel(db, novel)

# UPDATE
@router.patch("/{id}", response_model=NovelRead)
def novel_update(id: int, data: NovelUpdate, db: Session = Depends(get_db)):
    return update_novel(db, id, data)

# DELETE
@router.delete("/{id}", response_model = NovelRead)
def novel_delete(id: int, db: Session = Depends(get_db)):
    return delete_novel(db, id)

