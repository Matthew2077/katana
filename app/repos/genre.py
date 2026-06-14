from sqlalchemy import select
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from core.models import Genre
from typing import Dict

# READ
def get_genre_by_id(db: Session, id: int):
    stmt = select(Genre).where(Genre.id == id)
    result = db.execute(stmt)
    return result.scalar_one_or_none()

def get_genre_by_name(db: Session, name: str):
    stmt = select(Genre).where(Genre.name == name)
    result = db.execute(stmt)
    return result.scalar_one_or_none()

def get_genre_list(db: Session):
    stmt = select(Genre)
    result = db.execute(stmt)
    return result.scalars().all()

# SAVE
def save_genre(db: Session, genre: Genre):
    try:
        db.add(genre)
        db.commit()
        db.refresh(genre)
        return genre
    except:
        db.rollback()
        raise ValueError("Error saving genre on DB")
    
# UPDATE
def edit_genre(db: Session, genre: Genre, data: Dict):
    try:
        for field, value in data.items():
            setattr(genre, field, value) 
        db.commit()
        db.refresh(genre)
        return genre
    except:
        db.rollback()
        raise ValueError("Error updating  genre on DB")

# DELETE
def delete_genre(db: Session, genre: Genre):
    try:
        db.delete(genre)
        db.commit()
        return genre
    except:
        db.rollback()
        raise ValueError("Error deleting genre on DB")