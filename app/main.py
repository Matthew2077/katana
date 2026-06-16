from fastapi import FastAPI
from core import Base, engine
import logging
from fastapi.middleware.cors import CORSMiddleware
import logging

app = FastAPI(
    title="Katana API",
    version="1.0.0",
    description=""
)

# crea tutte le tabelle
Base.metadata.create_all(bind=engine)

# Routers
# app.include_router(note.router, prefix="", tags=[""])

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