from sqlmodel import SQLModel, Field

class Producte(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    nom: str
    cost: int
    quantitat: int
    proveedor: str
    ventes: int