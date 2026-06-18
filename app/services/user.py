from sqlalchemy.orm import Session
from repos.user import get_user_by_id, get_user_list, get_user_by_name, save_user, edit_user, erase_user
from core.models import User
from schemas.user import UserUpdate, UserCreate
from fastapi import HTTPException
import logging

logger = logging.getLogger(__name__)

# READ
def read_user_by_id(db: Session, id: int):
    try: 
        result = get_user_by_id(db, id)
        if result is None:
            raise HTTPException(status_code=404, detail=f"User {id} not found")
        
        return result
    except Exception as e:
        logger.info(f"id: {id}, Layer: services, usage: read id")
        logger.error(f"error: {e}", exc_info=True)

def read_user_by_name(db: Session, name: str):
    try: 
        result = get_user_by_name(db, name)
        if result is None:
            raise HTTPException(status_code=404, detail=f"User {name} not found")
        
        return result
    except Exception as e:
        logger.info(f"name: {name}, Layer: services, usage: read name")
        logger.error(f"error: {e}", exc_info=True)

def read_all_users(db: Session):
    try:
        result = get_user_list(db)
        if result is None:
            raise HTTPException(status_code=404, detail=f"DB has no users")
        
        return result
    except Exception as e:
        logger.info("Layer: services, usage: read all")
        logger.error(f"error: {e}", exc_info=True)

# CREATE NEW user
def create_user(db: Session, user: UserCreate):
    try:
        new_user = User(
            id = user.id,
            name = user.name
        )

        result = save_user(db, new_user)
        return result
    except Exception as e: 
        logger.info(f"Layer: services, usage: create, user: {user}")
        logger.error(f"error: {e}", exc_info=True)

# UPDATE user
def update_user(db: Session, user_id: int, data: UserUpdate):
    try:
        user = read_user_by_id(db, user_id)

        if user is None:
            logger.error(f"User {user_id} not found")
            raise HTTPException(status_code=404, detail=f"User {id} not found")
        
        update_data = data.model_dump(exclude_unset=True) # remove nones 

        result = edit_user(db, user, update_data) # update_data need to be a dict
        return result
    except Exception as e:
        logger.info(f"Layer: services, usage: update, data: {data}")
        logger.error(f"error: {e}", exc_info=True)

def delete_user(db: Session, user_id: int):
    try:
        user = read_user_by_id(db, user_id)
        if user is None:
            logger.error(f"User {user_id} not found")
            raise HTTPException(status_code=404, detail=f"User {id} not found")
        
        delete = erase_user(db, user)
        return user
    except Exception as e:
        logger.error(f"Layer: services, usage: delete, id: {user_id}")
        logger.error(f"error: {e}", exc_info=True)

