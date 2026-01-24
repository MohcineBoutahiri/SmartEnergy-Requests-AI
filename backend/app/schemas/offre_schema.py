from pydantic import BaseModel
from typing import Optional


# =========================
# CREATE / UPDATE
# =========================
class OffreRequest(BaseModel):
    nom: str
    type_energie: str
    prix_kwh: float
    duree_mois: int


class UpdateOffreRequest(BaseModel):
    nom: Optional[str] = None
    type_energie: Optional[str] = None
    prix_kwh: Optional[float] = None
    duree_mois: Optional[int] = None
    actif: Optional[bool] = None


# =========================
# RESPONSE
# =========================
class OffreResponse(BaseModel):
    id: int
    nom: str
    type_energie: str
    prix_kwh: float
    duree_mois: int
    actif: bool

    class Config:
        from_attributes = True
