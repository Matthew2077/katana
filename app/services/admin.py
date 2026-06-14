from sqlalchemy.orm import Session
from repos import get_admin_by_id, get_admin_list, get_admin_by_name

# READ
def read_admin_by_id(db: Session, id: int):
    try: 
        result = get_admin_by_id(db, id)
        return result
    except:
        raise ValueError(f"Errore placeholder. id: {id}, Layer: services, usage: read id")

def read_admin_by_name(db: Session, name: str):
    try: 
        result = get_admin_by_name(db, name)
        return result
    except:
        raise ValueError(f"Errore placeholder. name: {name}, Layer: services, usage: read name")

def get_all_admins(db):
    try:
        result = get_admin_list(db)
        return result
    except:
        raise ValueError(f"Errore placeholder. Layer: services, usage: read all")
