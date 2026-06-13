from sqlmodel import SQLModel

# crea tabelle
SQLModel.metadata.create_all(engine)
