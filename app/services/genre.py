from sqlalchemy.orm import Session
from repos.genre import get_genre_by_id, get_genre_by_name, get_genre_list, save_genre, edit_genre, erase_genre
from core.models import Genre
from schemas.genre import GenreCreate, GenreUpdate
from fastapi import HTTPException
import logging

logger = logging.getLogger(__name__)


# READ
def read_genre_by_id(db: Session, id: int):
    try: 
        result = get_genre_by_id(db, id)
        if result is None:
            raise HTTPException(status_code=404, detail=f"genre {id} not found")
        
        return result
    except Exception as e:
        logger.info(f"id: {id}, Layer: services, usage: read id")
        logger.error(f"error: {e}", exc_info=True)

def read_genre_by_name(db: Session, name: str):
    try: 
        result = get_genre_by_name(db, name)
        if result is None:
            raise HTTPException(status_code=404, detail=f"genre {name} not found")
        return result
    except Exception as e:
        logger.info(f"name: {name}, Layer: services, usage: read name")
        logger.error(f"error: {e}", exc_info=True)


def read_all_genre(db: Session):
    try:
        result = get_genre_list(db)
        if result is None:
            raise HTTPException(status_code=404, detail=f"DB has no genre")
        return result
    except Exception as e:
        logger.info("Layer: services, usage: read all")
        logger.error(f"error: {e}", exc_info=True)


# CREATE NEW
def create_genre(db: Session, genre: GenreCreate):
    try:
        new_genre = Genre(
            name = genre.name,
            label = genre.label
        )

        result = save_genre(db, new_genre)
        return result
    except Exception as e: 
        logger.info(f"Layer: services, usage: create, genre: {genre}")
        logger.error(f"error: {e}", exc_info=True)


# UPDATE 
def update_genre(db: Session, genre_id: int, data: GenreUpdate):
    try:
        # check if genre exist
        genre = read_genre_by_id(db, genre_id)
        if genre is None:
            logger.error(f"genre {genre} not found")
            raise HTTPException(status_code=404, detail=f"genre {id} not found")


        # update
        update_data = data.model_dump(exclude_unset=True) # remove nones 
        result = edit_genre(db, genre, update_data) # update_data need to be a dict
        return result
    
    except Exception as e:
        logger.info(f"Layer: services, usage: update, data: {data}")
        logger.error(f"error: {e}", exc_info=True)


def delete_genre(db: Session, genre_id: int):
    try:
        genre = read_genre_by_id(db, genre_id)
        if genre is None:
            logger.error(f"genre {genre_id} not found")
            raise HTTPException(status_code=404, detail=f"genre {id} not found")
        
        delete = erase_genre(db, genre)
        return genre
    
    except Exception as e:
        logger.error(f"Layer: services, usage: delete, id: {genre_id}")
        logger.error(f"error: {e}", exc_info=True)
