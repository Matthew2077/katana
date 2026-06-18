from fastapi import Depends, FastAPI
from fastapi import APIRouter
from sqlalchemy.orm import Session
from services.user import read_all_users, read_user_by_name, read_user_by_id, create_user, update_user, delete_user
from core.database import get_db
from schemas.user import UserCreate, UserRead, UserUpdate
from typing import List

router = APIRouter()