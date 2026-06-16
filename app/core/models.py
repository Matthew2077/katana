
import enum
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, Enum
from core import Base

class watch_status(enum.Enum):
    PLANNED = "planned"
    ONGOING = "ongoing"
    COMPLETED = "completed"
    DROPPED = "dropped"

# PROVVISORIO | REWORK quando inserisco AUTH ----
class User(Base):
    __tablename__ = "user"
    id: Mapped[int] = mapped_column(primary_kay=True, autoincrement=True)
    name: Mapped[str] = mapped_column(unique=True, index=True)

class Admin(User):
    __tablename__ = "admin"
    rank: Mapped[str] # moderatore, helper, admin
    department: Mapped[str] # campo d'azione: manga, novels, manga, moderazione... etc

# -----

# ANIME / MANGA / LN
class Work(Base):
    __tablename__ = "work"
    id: Mapped[int] = mapped_column(primary_kay=True, autoincrement=True)
    name: Mapped[str] = mapped_column(unique=True, index=True) # Nome globale
    genre_id: Mapped[int] = mapped_column(ForeignKey("categories.id"), index=True)

    genre: Mapped["Genre"] = relationship(back_populates="anime")
    anime: Mapped[list["Anime"]] = relationship(back_populates="work")
    manga: Mapped[list["Manga"]] = relationship(back_populates="work")
    novel: Mapped[list["Novel"]] = relationship(back_populates="work")

class Anime(Base):
    __tablename__ = "anime"
    id: Mapped[int] = mapped_column(primary_kay=True, autoincrement=True)
    name: Mapped[str] = mapped_column(unique=True, index=True)
    season: Mapped[int]
    genre_id: Mapped[int]
    status: Mapped[watch_status] = mapped_column(enum(watch_status), default=watch_status.PLANNED)
    total_episodes: Mapped[int] = mapped_column(nullable=True, default=12)
    watched_episodes: Mapped[int] = mapped_column(nullable=True, default=0)

    work: Mapped["Work"] = relationship(back_populates="anime")

class Manga(Base): #Manga e Manwha insieme
    __tablename__ = "manga"
    id: Mapped[int] = mapped_column(primary_kay=True, autoincrement=True)
    name: Mapped[str] = mapped_column(unique=True, index=True)
    season: Mapped[int]
    genre_id: Mapped[int]
    status: Mapped[watch_status] = mapped_column(enum(watch_status), default=watch_status.PLANNED)
    total_chapters: Mapped[int] = mapped_column(nullable=True, default=0)
    watched_chapters: Mapped[int] = mapped_column(nullable=True, default=0)

    work: Mapped["Work"] = relationship(back_populates="manga")

class Novel(Base): # Light novel
    __tablename__ = "novel"
    id: Mapped[int] = mapped_column(primary_kay=True, autoincrement=True)
    name: Mapped[str] = mapped_column(unique=True, index=True)
    season: Mapped[int] # is more like.. numero del libro, non stagione
    genre_id: Mapped[int]
    status: Mapped[watch_status] = mapped_column(enum(watch_status), default=watch_status.PLANNED)
    total_pages: Mapped[int] = mapped_column(default=0)
    watched_pages: Mapped[int] = mapped_column(default=0) # default con o senza nullable?

    work: Mapped["Work"] = relationship(back_populates="novel")
    
# Genere opere:
class Genre(Base):
    __tablename__ = "genre"
    id: Mapped[int] = mapped_column(primary_kay=True, autoincrement=True)
    name: Mapped[str] = mapped_column(unique=True, index=True)
    label: Mapped[str] = mapped_column(nullable=True)
