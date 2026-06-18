from sqlalchemy.orm import Session
from repos.novel import get_novel_by_id, get_novel_by_name, get_novel_list, save_novel, edit_novel, erase_novel
from core.models import Novel
from schemas.novel import NovelCreate, NovelUpdate
from fastapi import HTTPException
import logging

logger = logging.getLogger(__name__)
logging.basicConfig(filename='katana.log', level=logging.DEBUG)

# READ
def read_novel_by_id(db: Session, id: int):
    try: 
        result = get_novel_by_id(db, id)
        if result is None:
            raise HTTPException(status_code=404, detail=f"Novel {id} not found")
        
        return result
    except Exception as e:
        logger.info(f"id: {id}, Layer: services, usage: read id")
        logger.error(f"error: {e}", exc_info=True)

def read_novel_by_name(db: Session, name: str):
    try: 
        result = get_novel_by_name(db, name)
        if result is None:
            raise HTTPException(status_code=404, detail=f"Novel {name} not found")
        return result
    except Exception as e:
        logger.info(f"name: {name}, Layer: services, usage: read name")
        logger.error(f"error: {e}", exc_info=True)


def read_all_novel(db: Session):
    try:
        result = get_novel_list(db)
        return result
    except Exception as e:
        logger.info("Layer: services, usage: read all")
        logger.error(f"error: {e}", exc_info=True)


# CREATE NEW
def create_novel(db: Session, novel: NovelCreate):
    try:
        new_novel = Novel(
            id = novel.id,
            name = novel.name,
            season = novel.season,
            genre_id = novel.genre_id,
            total_pages = novel.total_pages,
            watched_pages = novel.watched_pages
        )

        result = save_novel(db, new_novel)
        return result
    except Exception as e: 
        logger.info(f"Layer: services, usage: create, novel: {novel}")
        logger.error(f"error: {e}", exc_info=True)


# UPDATE 
def update_novel(db: Session, novel_id: int, data: NovelUpdate):
    try:
        novel = read_novel_by_id(db, novel_id)

        if novel is None:
            logger.error(f"Novel {novel} not found")
            raise HTTPException(404)
        
        update_data = data.model_dump(exclude_unset=True) # remove nones 

        result = edit_novel(db, novel, update_data) # update_data need to be a dict
        return result
    
    except Exception as e:
        logger.info(f"Layer: services, usage: update, data: {data}")
        logger.error(f"error: {e}", exc_info=True)


def delete_novel(db: Session, novel_id: int):
    try:
        novel = read_novel_by_id(db, novel_id)
        if novel is None:
            logger.error(f"Novel {novel_id} not found")
            raise HTTPException(404)
        
        delete = erase_novel(db, novel)
        return novel
    
    except Exception as e:
        logger.error(f"Layer: services, usage: delete, id: {novel_id}")
        logger.error(f"error: {e}", exc_info=True)
