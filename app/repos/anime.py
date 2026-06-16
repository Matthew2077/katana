from sqlalchemy import select
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from core.models import Anime
from typing import Dict

# READ
def get_anime_by_id(db: Session, id: int):
    stmt = select(Anime).where(Anime.id == id)
    result = db.execute(stmt)
    return result.scalar_one_or_none()

def get_anime_by_name(db: Session, name: str):
    stmt = select(Anime).where(Anime.name == name)
    result = db.execute(stmt)
    return result.scalar_one_or_none()

def get_anime_list(db: Session):
    stmt = select(Anime)
    result = db.execute(stmt)
    return result.scalars().all()

# SAVE
def save_anime(db: Session, anime: Anime):
    try:
        db.add(anime)
        db.commit()
        db.refresh(anime)
        return anime
    except:
        db.rollback()
        raise ValueError("Error saving anime on DB")
    
# UPDATE
def edit_anime(db: Session, anime: Anime, data: Dict):
    try:
        for field, value in data.items():
            setattr(anime, field, value) 
        db.commit()
        db.refresh(anime)
        return anime
    except:
        db.rollback()
        raise ValueError("Error updating  anime on DB")

# DELETE
def erase_anime(db: Session, anime: Anime):
    try:
        db.delete(anime)
        db.commit()
        return anime
    except:
        db.rollback()
        raise ValueError("Error deleting anime on DB")