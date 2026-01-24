from pydantic import BaseModel
from typing import Optional


# =========================
# 🔹 UPDATE CLIENT (PUT)
# =========================
class UpdateClientRequest(BaseModel):
    telephone: Optional[str] = None
    adresse: Optional[str] = None


# =========================
# 🔹 RESPONSE CLIENT
# =========================
class ClientResponse(BaseModel):
    id: int
    telephone: Optional[str]
    adresse: Optional[str]
    utilisateur_id: int

    class Config:
        from_attributes = True
