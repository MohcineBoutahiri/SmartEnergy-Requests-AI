from pydantic import BaseModel
from datetime import date
from typing import Optional


# =========================
# CREATE CONTRAT (ADMIN)
# =========================
class CreateContratRequest(BaseModel):
    client_id: int
    offre_id: int
    date_debut: date
    date_fin: date


# =========================
# UPDATE STATUT
# =========================
class UpdateContratStatutRequest(BaseModel):
    statut: str


# =========================
# RESPONSE
# =========================
class ContratResponse(BaseModel):
    id: int
    reference: str
    client_id: int
    offre_id: int
    date_debut: date
    date_fin: date
    statut: str

    class Config:
        from_attributes = True
