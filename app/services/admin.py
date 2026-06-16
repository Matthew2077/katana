from sqlalchemy.orm import Session
from repos.admin import get_admin_by_id, get_admin_list, get_admin_by_name, save_admin, edit_admin, erase_admin
from core.models import Admin
from schemas.admin import AdminUpdate, AdminCreate
from fastapi import HTTPException
import logging

logger = logging.getLogger(__name__)
logging.basicConfig(filename='katana.log', level=logging.DEBUG)

# READ
def read_admin_by_id(db: Session, id: int):
    try: 
        result = get_admin_by_id(db, id)
        return result
    except Exception as e:
        logger.info(f"id: {id}, Layer: services, usage: read id")
        logger.error(f"error: {e}", exc_info=True)

def read_admin_by_name(db: Session, name: str):
    try: 
        result = get_admin_by_name(db, name)
        return result
    except Exception as e:
        logger.info(f"name: {name}, Layer: services, usage: read name")
        logger.error(f"error: {e}", exc_info=True)

def get_all_admins(db: Session):
    try:
        result = get_admin_list(db)
        return result
    except Exception as e:
        logger.info("Layer: services, usage: read all")
        logger.error(f"error: {e}", exc_info=True)

# CREATE NEW ADMIN
def create_admin(db: Session, admin: AdminCreate):
    try:
        new_admin = Admin(
            id = admin.id,
            name = admin.name,
            rank = admin.rank,
            department = admin.department
        )

        result = save_admin(db, new_admin)
        return result
    except Exception as e: 
        logger.info(f"Layer: services, usage: create, admin: {admin}")
        logger.error(f"error: {e}", exc_info=True)

# UPDATE ADMIN
def update_admin(db: Session, admin_id: int, data: AdminUpdate):
    try:
        admin = read_admin_by_id(db, admin_id)

        if admin is None:
            logger.error(f"Admin {admin_id} not found")
            raise HTTPException(404)
        
        update_data = data.model_dump(exclude_unset=True) # remove nones 

        result = edit_admin(db, admin, update_data) # update_data need to be a dict
        return result
    except Exception as e:
        logger.info(f"Layer: services, usage: update, data: {data}")
        logger.error(f"error: {e}", exc_info=True)

def delete_admin(db: Session, admin_id: int):
    try:
        admin = read_admin_by_id(db, admin_id)
        if admin is None:
            logger.error(f"Admin {admin_id} not found")
            raise HTTPException(404)
        
        delete = erase_admin(db, admin)
        return admin
    except Exception as e:
        logger.error(f"Layer: services, usage: delete, id: {admin_id}")
        logger.error(f"error: {e}", exc_info=True)

