
import enum
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, Enum
from core import Base

class anime_status(enum.Enum):
    PLANNED = "planned"
    ONGOING = "ongoing"
    COMPLETED = "completed"
    DROPPED = "dropped"

class User(Base):
    __tablename__ = "user"
    id: Mapped[int] = mapped_column(primary_kay=True, autoincrement=True)
    name: Mapped[str] = mapped_column(unique=True, index=True)

class Admin(User):
    __tablename__ = "admin"
    role: Mapped[str]
    department: Mapped[str]

class Anime(Base):
    __tablename__ = "anime"
    id: Mapped[int] = mapped_column(primary_kay=True, autoincrement=True)
    name: Mapped[str] = mapped_column(unique=True, index=True)
    season: Mapped[int]
    status: Mapped[anime_status] = mapped_column(enum(anime_status), default=anime_status.PLANNED)
    episodes_total: Mapped[int]
    episodes_watched: Mapped[int]
    genre_id: Mapped[int] = mapped_column(ForeignKey("categories.id"), index=True)

    genre: Mapped["Genre"] = relationship(back_populates="anime") 

class Genre(Base):
    __tablename__ = "genre"
    id: Mapped[int] = mapped_column(primary_kay=True, autoincrement=True)
    name: Mapped[str] = mapped_column(unique=True, index=True)
