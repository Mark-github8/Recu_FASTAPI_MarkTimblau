from fastapi import FastAPI
from sqlmodel import SQLModel, create_engine, Session, select
from dotenv import load_dotenv
from models.usuaris import usuaris
from schema.usuaris_sch import schema, schemas
import os


app = FastAPI()


load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")
engine = create_engine(DATABASE_URL)


SQLModel.metadata.create_all(engine)


def get_db():
   db = Session(engine)
   try:
       yield db
   finally:
       db.close()

#NOU USUARI
def afegir_usuaris(nom, cognom, edat, treball, alcada, database: Session):
    nou_usuari = usuaris(nom=nom, cognom=cognom, edat=edat, treball=treball, alcada=alcada)
    database.add(nou_usuari)
    database.commit()
    database.refresh(nou_usuari)

#LLEGIR PER ID
def leer_usuari(id: int, database: Session):
    statement = select(usuaris).where(usuaris.id == id)
    existencia = database.exec(statement).first()
    if existencia:
        return {
            "Result": existencia
        }