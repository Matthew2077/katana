from sqlalchemy.orm import Session
from repos.anime import get_anime_by_id, get_anime_by_name, get_anime_list, save_anime, edit_anime, erase_anime
from core.models import Anime
from schemas.anime import AnimeCreate, AnimeUpdate
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
def read_anime_by_id(db: Session, id: int):
    try: 
        result = get_anime_by_id(db, id)
        if result is None:
            raise HTTPException(status_code=404, detail=f"Anime {id} not found")
        
        return result
    except Exception as e:
        logger.info(f"id: {id}, Layer: services, usage: read id")
        logger.error(f"error: {e}", exc_info=True)
        raise HTTPException(status_code=500, detail="Internal server error")

def read_anime_by_name(db: Session, name: str):
    try: 
        result = get_anime_by_name(db, name)
        if result is None:
            raise HTTPException(status_code=404, detail=f"Anime {name} not found")
        
        return result
    except Exception as e:
        logger.info(f"name: {name}, Layer: services, usage: read name")
        logger.error(f"error: {e}", exc_info=True)
        raise HTTPException(status_code=500, detail="Internal server error")


def read_all_anime(db: Session):
    try:
        result = get_anime_list(db)
        if result is None:
            raise HTTPException(status_code=404, detail=f"DB has no anime")
        return result
    except Exception as e:
        logger.info("Layer: services, usage: read all")
        logger.error(f"error: {e}", exc_info=True)
        raise HTTPException(status_code=500, detail="Internal server error")


# CREATE NEW
def create_anime(db: Session, anime: AnimeCreate):
    try:
        new_anime = Anime(
            id = anime.id,
            name = anime.name,
            season = anime.season,
            genre_id = anime.genre_id,
            total_episodes = anime.total_episodes,
            watched_episodes = anime.watched_episodes
        )

        result = save_anime(db, new_anime)
        return result
    except Exception as e: 
        logger.info(f"Layer: services, usage: create, anime: {anime}")
        logger.error(f"error: {e}", exc_info=True)
        raise HTTPException(status_code=500, detail="Internal server error")


# UPDATE 
def update_anime(db: Session, anime_id: int, data: AnimeUpdate):
    try:
        # check if anime exist
        anime = read_anime_by_id(db, anime_id)
        if anime is None:
            logger.error(f"Anime {anime_id} not found")
            raise HTTPException(status_code=404, detail=f"Anime {anime_id} not found")
        
        # check if genre exist
        check_genre_exists(db, data.genre_id)

        # update
        update_data = data.model_dump(exclude_unset=True) # remove nones 
        result = edit_anime(db, anime, update_data) # update_data need to be a dict
        return result
    
    except Exception as e:
        logger.info(f"Layer: services, usage: update, data: {data}")
        logger.error(f"error: {e}", exc_info=True)
        raise HTTPException(status_code=500, detail="Internal server error")


def delete_anime(db: Session, anime_id: int):
    try:
        anime = read_anime_by_id(db, anime_id)
        if anime is None:
            logger.error(f"Anime {anime_id} not found")
            raise HTTPException(status_code=404, detail=f"Anime {id} not found")
        
        delete = erase_anime(db, anime)
        return anime
    
    except Exception as e:
        logger.error(f"Layer: services, usage: delete, id: {anime_id}")
        logger.error(f"error: {e}", exc_info=True)
        raise HTTPException(status_code=500, detail="Internal server error")
