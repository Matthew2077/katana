from sqlalchemy.orm import Session
from repos import get_user_by_id, get_user_by_name

def read_user(db: Session, id: int):
    if not id:
        raise ValueError(f"User id {id} invalid")
    
    anime = get_user_by_id(db, id)
    return anime
    