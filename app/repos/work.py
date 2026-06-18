from sqlalchemy import select
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from core.models import Work
from typing import Dict

# READ
def get_work_by_id(db: Session, id: int):
    stmt = select(Work).where(Work.id == id)
    result = db.execute(stmt)
    return result.scalar_one_or_none()

def get_work_by_name(db: Session, name: str):
    stmt = select(Work).where(Work.name == name)
    result = db.execute(stmt)
    return result.scalar_one_or_none()
  
def get_work_list(db: Session):
    stmt = select(Work)
    result = db.execute(stmt)
    return result.scalars().all()

# SAVE
def save_work(db: Session, work: Work):
    try:
        db.add(work)
        db.commit()
        db.refresh(work)
        return work
    except:
        db.rollback()
        raise ValueError("Error saving work on DB")
    
# UPDATE
def edit_work(db: Session, work: Work, data: Dict):
    try:
        for field, value in data.items():
            setattr(work, field, value) 
        db.commit()
        db.refresh(work)
        return work
    except:
        db.rollback()
        raise ValueError("Error updating  work on DB")

# DELETE
def erase_work(db: Session, work: Work):
    try:
        db.delete(work)
        db.commit()
        return work
    except:
        db.rollback()
        raise ValueError("Error deleting work on DB")