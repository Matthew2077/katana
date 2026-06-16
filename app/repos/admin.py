from sqlalchemy import select
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from core.models import Admin
from typing import Dict

# READ
def get_admin_by_id(db: Session, id: int):
    stmt = select(Admin).where(Admin.id == id)
    result = db.execute(stmt)
    return result.scalar_one_or_none()

def get_admin_by_name(db: Session, name: str):
    stmt = select(Admin).where(Admin.name == name)
    result = db.execute(stmt)
    return result.scalar_one_or_none()

def get_admin_list(db: Session):
    stmt = select(Admin)
    result = db.execute(stmt)
    return result.scalars().all()

def save_admin(db: Session, admin: Admin):
    try:
        db.add(admin)
        db.commit()
        db.refresh(admin)
        return admin
    except:
        db.rollback()
        raise ValueError("Error saving admin on DB")
    
# UPDATE
def edit_admin(db: Session, admin: Admin, data: Dict):
    try:
        for field, value in data.items():
            setattr(admin, field, value) 
        db.commit()
        db.refresh(admin)
        return admin
    except:
        db.rollback()
        raise ValueError("Error updating admin on DB")

# DELETE
def erase_admin(db: Session, admin: Admin):
    try:
        db.delete(admin)
        db.commit()
        return admin
    except:
        db.rollback()
        raise ValueError("Error deleting admin on DB")