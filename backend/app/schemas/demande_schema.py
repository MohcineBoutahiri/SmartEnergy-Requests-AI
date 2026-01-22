from pydantic import BaseModel

class DemandeCreate(BaseModel):
    message: str
    client_id: int

class DemandeResponse(DemandeCreate):
    id: int
    statut: str

    class Config:
        orm_mode = True
