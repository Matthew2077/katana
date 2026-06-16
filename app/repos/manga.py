from sqlalchemy import select
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from core.models import Manga
from typing import Dict

# READ
def get_manga_by_id(db: Session, id: int):
    stmt = select(Manga).where(Manga.id == id)
    result = db.execute(stmt)
    return result.scalar_one_or_none()

def get_manga_by_name(db: Session, name: str):
    stmt = select(Manga).where(Manga.name == name)
    result = db.execute(stmt)
    return result.scalar_one_or_none()

def get_manga_list(db: Session):
    stmt = select(Manga)
    result = db.execute(stmt)
    return result.scalars().all()

def save_manga(db: Session, manga: Manga):
    try:
        db.add(manga)
        db.commit()
        db.refresh(manga)
        return manga
    except:
        db.rollback()
        raise ValueError("Error saving manga on DB")
    

# SAVE
def save_manga(db: Session, manga: Manga):
    try:
        db.add(manga)
        db.commit()
        db.refresh(manga)
        return manga
    except:
        db.rollback()
        raise ValueError("Error saving manga on DB")
    
# UPDATE
def edit_manga(db: Session, manga: Manga, data: Dict):
    try:
        for field, value in data.items():
            setattr(manga, field, value) 
        db.commit()
        db.refresh(manga)
        return manga
    except:
        db.rollback()
        raise ValueError("Error updating  manga on DB")

# DELETE
def erase_manga(db: Session, manga: Manga):
    try:
        db.delete(manga)
        db.commit()
        return manga
    except:
        db.rollback()
        raise ValueError("Error deleting manga on DB")