from sqlalchemy import select
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from core.models import Novel
from typing import Dict

# READ
def get_novel_by_id(db: Session, id: int):
    stmt = select(Novel).where(Novel.id == id)
    result = db.execute(stmt)
    return result.scalar_one_or_none()

def get_novel_by_name(db: Session, name: str):
    stmt = select(Novel).where(Novel.name == name)
    result = db.execute(stmt)
    return result.scalar_one_or_none()

def get_novel_list(db: Session):
    stmt = select(Novel)
    result = db.execute(stmt)
    return result.scalars().all()

def save_novel(db: Session, novel: Novel):
    try:
        db.add(novel)
        db.commit()
        db.refresh(novel)
        return novel
    except:
        db.rollback()
        raise ValueError("Error saving novel on DB")
    

# SAVE
def save_novel(db: Session, novel: Novel):
    try:
        db.add(novel)
        db.commit()
        db.refresh(novel)
        return novel
    except:
        db.rollback()
        raise ValueError("Error saving novel on DB")
    
# UPDATE
def edit_novel(db: Session, novel: Novel, data: Dict):
    try:
        for field, value in data.items():
            setattr(novel, field, value) 
        db.commit()
        db.refresh(novel)
        return novel
    except:
        db.rollback()
        raise ValueError("Error updating  novel on DB")

# DELETE
def erase_novel(db: Session, novel: Novel):
    try:
        db.delete(novel)
        db.commit()
        return novel
    except:
        db.rollback()
        raise ValueError("Error deleting novel on DB")