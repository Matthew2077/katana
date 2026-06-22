from sqlalchemy.orm import Session
from repos.manga import get_manga_by_id, get_manga_by_name, get_manga_list, save_manga, edit_manga, erase_manga
from core.models import Manga
from repos.work import get_work_by_id
from schemas.manga import MangaCreate, MangaUpdate
from fastapi import HTTPException
from repos.genre import get_genre_by_id
from schemas.genre import GenreRead
import logging

logger = logging.getLogger(__name__)

def check_genre_exists(db: Session, genre_id: int) -> GenreRead:
    genre = get_genre_by_id(db, genre_id)
    if genre is None:
        raise HTTPException(status_code=404, detail=f"Genre {genre_id} not found")
    return genre

# READ
def read_manga_by_id(db: Session, id: int):
    try: 
        result = get_manga_by_id(db, id)
        if result is None:
            raise HTTPException(status_code=404, detail=f"Manga {id} not found")
        
        return result
    except Exception as e:
        logger.info(f"id: {id}, Layer: services, usage: read id")
        logger.error(f"error: {e}", exc_info=True)
        raise HTTPException(status_code=500, detail="Internal server error")

def read_manga_by_name(db: Session, name: str):
    try: 
        result = get_manga_by_name(db, name)
        if result is None:
            raise HTTPException(status_code=404, detail=f"Manga {name} not found")
        return result
    except Exception as e:
        logger.info(f"name: {name}, Layer: services, usage: read name")
        logger.error(f"error: {e}", exc_info=True)
        raise HTTPException(status_code=500, detail="Internal server error")


def read_all_manga(db: Session):
    try:
        result = get_manga_list(db)
        if result is None:
            raise HTTPException(status_code=404, detail=f"DB has no manga")
        return result
    except Exception as e:
        logger.info("Layer: services, usage: read all")
        logger.error(f"error: {e}", exc_info=True)
        raise HTTPException(status_code=500, detail="Internal server error")


# CREATE NEW
def create_manga(db: Session, manga: MangaCreate):
    try:
        # check if work exist
        work = get_work_by_id(db, manga.work_id)
        if work is None:
            raise HTTPException(status_code=404, detail=f"work {manga.work_id} not found")
        
        # check if genre exist
        check_genre_exists(db, manga.genre_id)

        new_manga = Manga(
            name = manga.name,
            season = manga.season,
            genre_id = manga.genre_id,
            work_id = manga.work_id,
            total_chapters = manga.total_chapters,
            watched_chapters = manga.watched_chapters
        )

        result = save_manga(db, new_manga)
        return result
    except Exception as e: 
        logger.info(f"Layer: services, usage: create, manga: {manga}")
        logger.error(f"error: {e}", exc_info=True)
        raise HTTPException(status_code=500, detail="Internal server error")


# UPDATE 
def update_manga(db: Session, manga_id: int, data: MangaUpdate):
    try:
        # check if manga exist
        manga = read_manga_by_id(db, manga_id)
        if manga is None:
            logger.error(f"Manga {manga} not found")
            raise HTTPException(status_code=404, detail=f"Manga {id} not found")
        
        # check if genre exist
        check_genre_exists(db, data.genre_id)

        # update
        update_data = data.model_dump(exclude_unset=True) # remove nones 
        result = edit_manga(db, manga, update_data) # update_data need to be a dict
        return result
    
    except Exception as e:
        logger.info(f"Layer: services, usage: update, data: {data}")
        logger.error(f"error: {e}", exc_info=True)
        raise HTTPException(status_code=500, detail="Internal server error")


def delete_manga(db: Session, manga_id: int):
    try:
        manga = read_manga_by_id(db, manga_id)
        if manga is None:
            logger.error(f"Manga {manga_id} not found")
            raise HTTPException(status_code=404, detail=f"Manga {id} not found")
        
        delete = erase_manga(db, manga)
        return manga
    
    except Exception as e:
        logger.error(f"Layer: services, usage: delete, id: {manga_id}")
        logger.error(f"error: {e}", exc_info=True)
        raise HTTPException(status_code=500, detail="Internal server error")
