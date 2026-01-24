from pydantic import BaseModel
from typing import Optional
from datetime import datetime


# =========================
# 🔹 CREATE DEMANDE
# =========================
class CreateDemandeRequest(BaseModel):
    message: str
    type_demande: Optional[str]


# =========================
# 🔹 UPDATE STATUT (ADMIN)
# =========================
class UpdateStatutRequest(BaseModel):
    statut: str


# =========================
# 🔹 RESPONSE DEMANDE
# =========================
class DemandeResponse(BaseModel):
    id: int
    client_id: int
    message: str
    type_demande: Optional[str]
    statut: str
    date_creation: datetime

    class Config:
        from_attributes = True
