from fastapi import FastAPI
from sqlmodel import SQLModel, create_engine, Session
from dotenv import load_dotenv
from models.usuaris import usuaris
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
