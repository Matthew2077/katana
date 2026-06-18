from sqlalchemy.orm import Session
from repos.manga import get_manga_by_id, get_manga_by_name, get_manga_list, save_manga, edit_manga, erase_manga
from core.models import Manga
from schemas.manga import MangaCreate, MangaUpdate
from fastapi import HTTPException
import logging

logger = logging.getLogger(__name__)
logging.basicConfig(filename='katana.log', level=logging.DEBUG)

# READ
def read_manga_by_id(db: Session, id: int):
    try: 
        result = get_manga_by_id(db, id)
        return result
    except Exception as e:
        logger.info(f"id: {id}, Layer: services, usage: read id")
        logger.error(f"error: {e}", exc_info=True)

def read_manga_by_name(db: Session, name: str):
    try: 
        result = get_manga_by_name(db, name)
        return result
    except Exception as e:
        logger.info(f"name: {name}, Layer: services, usage: read name")
        logger.error(f"error: {e}", exc_info=True)


def get_all_manga(db: Session):
    try:
        result = get_manga_list(db)
        return result
    except Exception as e:
        logger.info("Layer: services, usage: read all")
        logger.error(f"error: {e}", exc_info=True)


# CREATE NEW
def create_manga(db: Session, manga: MangaCreate):
    try:
        new_manga = Manga(
            id = manga.id,
            name = manga.name,
            season = manga.season,
            genre_id = manga.genre_id,
            total_chapters = manga.total_chapters,
            watched_chapters = manga.watched_chapters
        )

        result = save_manga(db, new_manga)
        return result
    except Exception as e: 
        logger.info(f"Layer: services, usage: create, manga: {manga}")
        logger.error(f"error: {e}", exc_info=True)


# UPDATE 
def update_manga(db: Session, manga_id: int, data: MangaUpdate):
    try:
        manga = read_manga_by_id(db, manga_id)

        if manga is None:
            logger.error(f"Manga {manga} not found")
            raise HTTPException(404)
        
        update_data = data.model_dump(exclude_unset=True) # remove nones 

        result = edit_manga(db, manga, update_data) # update_data need to be a dict
        return result
    
    except Exception as e:
        logger.info(f"Layer: services, usage: update, data: {data}")
        logger.error(f"error: {e}", exc_info=True)


def delete_manga(db: Session, manga_id: int):
    try:
        manga = read_manga_by_id(db, manga_id)
        if manga is None:
            logger.error(f"Manga {manga_id} not found")
            raise HTTPException(404)
        
        delete = erase_manga(db, manga)
        return manga
    
    except Exception as e:
        logger.error(f"Layer: services, usage: delete, id: {manga_id}")
        logger.error(f"error: {e}", exc_info=True)
