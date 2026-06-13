from sqlalchemy.orm import Session
from repos import get_anime_by_id, get_anime_by_name, save_anime, edit_anime, delete_anime

def read_anime(db: Session, id: int):
    if not id:
        raise ValueError(f"Anime id {id} invalid")
    
    anime = get_anime_by_id(db, id)
    return anime
    