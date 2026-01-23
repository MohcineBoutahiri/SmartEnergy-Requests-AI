from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.models.utilisateur import Utilisateur
from app.auth.password import verify_password, hash_password
from app.auth.jwt import create_access_token
from app.schemas.auth_schema import LoginRequest, RegisterRequest

router = APIRouter(prefix="/auth", tags=["Auth"])


# =========================
# LOGIN
# =========================
@router.post("/login")
def login(data: LoginRequest, db: Session = Depends(get_db)):
    user = db.query(Utilisateur).filter(
        Utilisateur.email == data.email
    ).first()

    if not user or not verify_password(data.password, user.mot_de_passe):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Identifiants invalides"
        )

    token = create_access_token({
        "user_id": user.id,
        "email": user.email,
        "role": user.role_id  # CLIENT / AGENT / ADMIN
    })

    return {
        "access_token": token,
        "token_type": "bearer"
    }


# =========================
# REGISTER (CLIENT ONLY)
# =========================
@router.post("/register", status_code=status.HTTP_201_CREATED)
def register(data: RegisterRequest, db: Session = Depends(get_db)):
    # 1️⃣ Vérifier si l'email existe déjà
    existing_user = db.query(Utilisateur).filter(
        Utilisateur.email == data.email
    ).first()

    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email déjà utilisé"
        )

    # 2️⃣ Créer un utilisateur CLIENT
    new_user = Utilisateur(
        nom=data.nom,
        email=data.email,
        mot_de_passe=hash_password(data.password),
        role_id=1,  # ROLE CLIENT
        actif=True
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {
        "message": "Inscription client réussie",
        "email": new_user.email
    }


# =========================
# LOGOUT (OPTIONNEL)
# =========================
@router.post("/logout")
def logout():
    # En JWT stateless, le logout est généralement géré côté frontend
    return {"message": "Déconnexion réussie"}
