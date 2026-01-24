from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.models.utilisateur import Utilisateur
from app.models.client import Client
from app.auth.password import hash_password, verify_password
from app.auth.jwt import create_access_token
from app.schemas.auth_schema import LoginRequest, RegisterRequest

router = APIRouter(prefix="/auth", tags=["Auth"])


# =========================
# LOGIN
# =========================
@router.post("/login")
def login(data: LoginRequest, db: Session = Depends(get_db)):
    try:
        user = Utilisateur.get_by_email(db, data.email)

        if not user or not verify_password(data.password, user.mot_de_passe):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Identifiants invalides"
            )

        token = create_access_token({
            "user_id": user.id,
            "email": user.email,
            "role": user.role_id
        })

        return {
            "access_token": token,
            "token_type": "bearer"
        }

    except HTTPException:
        raise
    except Exception as e:
        print("❌ LOGIN ERROR:", e)
        raise HTTPException(500, "Erreur interne lors du login")


# =========================
# REGISTER (CLIENT)
# =========================
@router.post("/register", status_code=status.HTTP_201_CREATED)
def register(data: RegisterRequest, db: Session = Depends(get_db)):
    try:
        if Utilisateur.get_by_email(db, data.email):
            raise HTTPException(400, "Email déjà utilisé")

        user = Utilisateur.create(
            db=db,
            nom=data.nom,
            email=data.email,
            mot_de_passe=hash_password(data.password),
            role_id=1  # CLIENT
        )

        # création automatique du client
        Client.create(db=db, utilisateur_id=user.id)

        return {
            "message": "Inscription client réussie",
            "email": user.email
        }

    except HTTPException:
        raise
    except Exception as e:
        print("❌ REGISTER ERROR:", e)
        raise HTTPException(500, "Erreur interne lors de l'inscription")
