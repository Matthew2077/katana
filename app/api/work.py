from fastapi import Depends, FastAPI
from fastapi import APIRouter
from sqlalchemy.orm import Session
from services.work import read_all_work, read_work_by_name, read_work_by_id, create_work, update_work, delete_work
from core.database import get_db
from schemas.work import WorkCreate, WorkRead, WorkUpdate
from typing import List

router = APIRouter()

# READ 
@router.get("/{id}", response_model=WorkRead)
def work_read_by_id(id: int, db: Session = Depends(get_db)):
    return read_work_by_id(db, id)

@router.get("/{name}", response_model=WorkRead)
def work_read_by_name(name: str, db: Session = Depends(get_db)):
    return read_work_by_name(db, name)


@router.post("/", response_model=WorkRead)
def work_create(work: WorkCreate, db: Session = Depends(get_db)):
    return create_work(db, work)


@router.patch("/{id}", response_model=WorkRead)
def work_update(id: int, data: WorkUpdate, db: Session = Depends(get_db)):
    return update_work(db, id, data)

@router.delete("/{id}", response_model = WorkRead)
def work_delete(id: int, db: Session = Depends(get_db)):
    return delete_work(db, id)
