from sqlalchemy.orm import Session
from repos.work import get_work_by_id, get_work_by_name, get_work_list, save_work, edit_work, erase_work
from repos.genre import get_genre_by_id
from core.models import Work
from schemas.work import WorkCreate, WorkUpdate
from fastapi import HTTPException
import logging

logger = logging.getLogger(__name__)
logging.basicConfig(filename='katana.log', level=logging.DEBUG)

# READ
def read_work_by_id(db: Session, id: int):
    try: 
        result = get_work_by_id(db, id)
        if result is None:
            raise HTTPException(status_code=404, detail=f"Work {id} not found")
        
        return result
    except Exception as e:
        logger.info(f"id: {id}, Layer: services, usage: read id")
        logger.error(f"error: {e}", exc_info=True)

def read_work_by_name(db: Session, name: str):
    try: 
        result = get_work_by_name(db, name)
        if result is None:
            raise HTTPException(status_code=404, detail=f"Work {name} not found")
        
        return result
    except Exception as e:
        logger.info(f"name: {name}, Layer: services, usage: read name")
        logger.error(f"error: {e}", exc_info=True)


def read_all_work(db: Session):
    try:
        result = get_work_list(db)
        return result
    except Exception as e:
        logger.info("Layer: services, usage: read all")
        logger.error(f"error: {e}", exc_info=True)


# CREATE NEW
def create_work(db: Session, work: WorkCreate):
    try:
        genre = get_genre_by_id(db, work.genre_id)
        if genre is None:
            raise HTTPException(status_code=404, detail=f"Genre {work.genre_id} not found")
            

        new_work = Work(
            name = work.name,
            genre_id = work.genre_id
        )

        result = save_work(db, new_work)
        return result
    except Exception as e: 
        logger.info(f"Layer: services, usage: create, work: {work}")
        logger.error(f"error: {e}", exc_info=True)


# UPDATE 
def update_work(db: Session, work_id: int, data: WorkUpdate):
    try:
        # check if work exist
        work = read_work_by_id(db, work_id)
        if work is None:
            logger.error(f"Work {work} not found")
            raise HTTPException(status_code=404, detail=f"Work {work_id} not found")
        
        # check if genre exist
        genre = get_genre_by_id(db, data.genre_id)
        if genre is None:
            raise HTTPException(status_code=404, detail=f"Genre {work.genre_id} not found")
        
        # update obj
        update_data = data.model_dump(exclude_unset=True) # remove nones 
        result = edit_work(db, work, update_data) # update_data need to be a dict
        return result
    
    except Exception as e:
        logger.info(f"Layer: services, usage: update, data: {data}")
        logger.error(f"error: {e}", exc_info=True)


def delete_work(db: Session, work_id: int):
    try:
        work = read_work_by_id(db, work_id)
        if work is None:
            logger.error(f"Work {work_id} not found")
            raise HTTPException(status_code=404, detail=f"Work {work_id} not found")
        
        delete = erase_work(db, work)
        return work
    
    except Exception as e:
        logger.error(f"Layer: services, usage: delete, id: {work_id}")
        logger.error(f"error: {e}", exc_info=True)
