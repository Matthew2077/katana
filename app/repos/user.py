from sqlalchemy import select
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from core.models import User, Admin
from typing import Dict


def get_user_by_id(db: Session, id: int):
    stmt = select(User).where(User.id == id)
    result = db.execute(stmt)
    return result.scalar_one_or_none()

def get_user_by_name(db:Session, name: str):
    stmt = select(User).where(User.name == name)
    result = db.execute(stmt)
    return result.scalar_one_or_none()

def get_admin_by_id(db: Session, id: int):
    stmt = select(Admin).where(Admin.id == id)
    result = db.execute(stmt)
    return result.scalar_one_or_none()

def get_admin_by_name(db: Session, name: str):
    stmt = select(Admin).where(Admin.name == name)
    result = db.execute(stmt)
    return result.scalar_one_or_none()

def save_user(db: Session, user: User):
    try:
        db.add(user)
        db.commit()
        db.refresh(user)
        return user
    except:
        db.rollback()
        raise ValueError("Error saving user on DB")
    
# UPDATE
def edit_user(db: Session, user: User, data: Dict):
    try:
        for field, value in data.items():
            setattr(user, field, value) 
        db.commit()
        db.refresh(user)
        return user
    except:
        db.rollback()
        raise ValueError("Error updating user on DB")

# DELETE
def delete_user(db: Session, user: User):
    try:
        db.delete(user)
        db.commit()
        return user
    except:
        db.rollback()
        raise ValueError("Error deleting user on DB")