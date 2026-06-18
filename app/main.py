from fastapi import FastAPI
from core.database import Base, engine
import logging
from fastapi.middleware.cors import CORSMiddleware
from api import work, anime, manga, novel, genre, admin, user


app = FastAPI(
    title="Katana API",
    version="1.0.0",
    description=""
)

# crea tutte le tabelle
Base.metadata.create_all(bind=engine)

# Routers
app.include_router(work.router, prefix="/api/work", tags=["work"])
app.include_router(novel.router, prefix="/api/novel", tags=["novel"])
app.include_router(manga.router, prefix="/api/manga", tags=["manga"])
app.include_router(anime.router, prefix="/api/anime", tags=["anime"])

app.include_router(genre.router, prefix="/api/genre", tags=["genre"])
# app.include_router(user.router, prefix="/api/user", tags=["user"])
# app.include_router(admin.router, prefix="/api/admin", tags=["admin"])

@app.get("/")
def root():
    return {"message": "Katana API is running"}


# CORS FOR FRONTEND
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],      # in sviluppo va bene così
    allow_methods=["*"],
    allow_headers=["*"],
)

# LOGGING SETUP
logger = logging.getLogger(__name__)
logging.basicConfig(filename='katana.log', level=logging.DEBUG)
logger.info('Katana Started')


