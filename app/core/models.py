import enum
from typing import Optional
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, Enum
from core.database import Base


class WatchStatus(enum.Enum):
    PLANNED = "planned"
    ONGOING = "ongoing"
    COMPLETED = "completed"
    DROPPED = "dropped"


class User(Base):
    __tablename__ = "user"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True, index=True)
    name: Mapped[str] = mapped_column(unique=True, index=True)


class Admin(Base):
    __tablename__ = "admin"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True, index=True)
    name: Mapped[str] = mapped_column(unique=True, index=True)
    rank: Mapped[str]
    department: Mapped[str]


class Genre(Base):
    __tablename__ = "genre"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(unique=True, index=True)
    label: Mapped[Optional[str]] = mapped_column(default=None)  # fix nullable
    works: Mapped[list["Work"]] = relationship(back_populates="genre")  # fix back_populates


class Work(Base):
    __tablename__ = "work"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(unique=True, index=True)
    genre_id: Mapped[int] = mapped_column(ForeignKey("genre.id"), index=True)
    genre: Mapped["Genre"] = relationship(back_populates="works")  # fix plurale
    anime: Mapped[list["Anime"]] = relationship(back_populates="work")
    manga: Mapped[list["Manga"]] = relationship(back_populates="work")
    novel: Mapped[list["Novel"]] = relationship(back_populates="work")


class Anime(Base):
    __tablename__ = "anime"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(unique=True, index=True)
    season: Mapped[int]
    work_id: Mapped[int] = mapped_column(ForeignKey("work.id"), index=True)  # fix FK
    genre_id: Mapped[int] = mapped_column(ForeignKey("genre.id"), index=True)  # fix FK
    status: Mapped[WatchStatus] = mapped_column(Enum(WatchStatus), default=WatchStatus.PLANNED)
    total_episodes: Mapped[Optional[int]] = mapped_column(default=12)  # fix Optional
    watched_episodes: Mapped[Optional[int]] = mapped_column(default=0)
    work: Mapped["Work"] = relationship(back_populates="anime")


class Manga(Base):
    __tablename__ = "manga"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(unique=True, index=True)
    season: Mapped[int]
    work_id: Mapped[int] = mapped_column(ForeignKey("work.id"), index=True)
    genre_id: Mapped[int] = mapped_column(ForeignKey("genre.id"), index=True)
    status: Mapped[WatchStatus] = mapped_column(Enum(WatchStatus), default=WatchStatus.PLANNED)
    total_chapters: Mapped[Optional[int]] = mapped_column(default=0)
    watched_chapters: Mapped[Optional[int]] = mapped_column(default=0)
    work: Mapped["Work"] = relationship(back_populates="manga")


class Novel(Base):
    __tablename__ = "novel"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(unique=True, index=True)
    volume: Mapped[int]  # rinominato da season
    work_id: Mapped[int] = mapped_column(ForeignKey("work.id"), index=True)
    genre_id: Mapped[int] = mapped_column(ForeignKey("genre.id"), index=True)
    status: Mapped[WatchStatus] = mapped_column(Enum(WatchStatus), default=WatchStatus.PLANNED)
    total_pages: Mapped[int] = mapped_column(default=0)
    watched_pages: Mapped[int] = mapped_column(default=0)
    work: Mapped["Work"] = relationship(back_populates="novel")