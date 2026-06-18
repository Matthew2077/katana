from fastapi import Depends, FastAPI
from fastapi import APIRouter
from sqlalchemy.orm import Session
from services.admin import read_all_admins, read_admin_by_name, read_admin_by_id, create_admin, update_admin, delete_admin
from core.database import get_db
from schemas.admin import AdminCreate, AdminRead, AdminUpdate
from typing import List

router = APIRouter()


# READ 
@router.get("/{id}", response_model=AdminRead)
def admin_read_by_id(id: int, db: Session = Depends(get_db)):
    return read_admin_by_id(db, id)

@router.get("/{name}", response_model=AdminRead)
def admin_read_by_name(name: str, db: Session = Depends(get_db)):
    return read_admin_by_name(db, name)

@router.get("/", response_model=List[AdminRead])
def admin_read_all(db: Session = Depends(get_db)):
    return read_all_admins(db)

# CREATE
@router.post("/", response_model=AdminRead)
def admin_create(admin: AdminCreate, db: Session = Depends(get_db)):
    return create_admin(db, admin)

# UPDATE
@router.patch("/{id}", response_model=AdminRead)
def admin_update(id: int, data: AdminUpdate, db: Session = Depends(get_db)):
    return update_admin(db, id, data)

# DELETE
@router.delete("/{id}", response_model = AdminRead)
def admin_delete(id: int, db: Session = Depends(get_db)):
    return delete_admin(db, id)
