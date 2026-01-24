from pydantic import BaseModel
from typing import Optional


# =========================
# 🔹 CREATE UTILISATEUR
# =========================
class CreateUserRequest(BaseModel):
    nom: str
    email: str
    password: str
    role_id: int


# =========================
# 🔹 UPDATE UTILISATEUR
# =========================
class UpdateUserRequest(BaseModel):
    nom: Optional[str] = None
    email: Optional[str] = None
    role_id: Optional[int] = None
    actif: Optional[bool] = None


# =========================
# 🔹 RESPONSE UTILISATEUR
# =========================
class UserResponse(BaseModel):
    id: int
    nom: str
    email: str
    actif: bool
    role_id: int

    class Config:
        from_attributes = True
