from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from app.core.database import get_db
from app.auth.dependencies import require_admin

from app.models.utilisateur import Utilisateur
from app.models.client import Client
from app.models.demande import Demande
from app.models.offre import Offre
from app.models.contrat import Contrat

from app.schemas.utilisateur_schema import (
    CreateUserRequest,
    UpdateUserRequest,
    UserResponse
)
from app.schemas.client_schema import ClientResponse
from app.schemas.demande_schema import (
    DemandeResponse,
    UpdateStatutRequest
)
from app.schemas.offre_schema import (
    OffreRequest,
    UpdateOffreRequest,
    OffreResponse
)
from app.schemas.contrat_schema import (
    CreateContratRequest,
    UpdateContratStatutRequest,
    ContratResponse
)

router = APIRouter(prefix="/admin", tags=["Admin"])


# =====================================================
# 🟦 SECTION 1 — GESTION DES UTILISATEURS
# =====================================================

@router.get("/users", response_model=List[UserResponse])
def list_users(
    db: Session = Depends(get_db),
    admin=Depends(require_admin)
):
    return Utilisateur.get_all(db)


@router.post("/users", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def create_user(
    data: CreateUserRequest,
    db: Session = Depends(get_db),
    admin=Depends(require_admin)
):
    if Utilisateur.get_by_email(db, data.email):
        raise HTTPException(400, "Email déjà utilisé")

    return Utilisateur.create(
        db=db,
        nom=data.nom,
        email=data.email,
        mot_de_passe=data.password,
        role_id=data.role_id
    )


@router.put("/users/{user_id}", response_model=UserResponse)
def update_user(
    user_id: int,
    data: UpdateUserRequest,
    db: Session = Depends(get_db),
    admin=Depends(require_admin)
):
    user = Utilisateur.update(db, user_id, **data.dict(exclude_unset=True))
    if not user:
        raise HTTPException(404, "Utilisateur introuvable")
    return user


@router.delete("/users/{user_id}")
def delete_user(
    user_id: int,
    db: Session = Depends(get_db),
    admin=Depends(require_admin)
):
    if not Utilisateur.delete(db, user_id):
        raise HTTPException(404, "Utilisateur introuvable")

    return {"message": "Utilisateur supprimé"}


# =====================================================
# 🟦 SECTION 2 — GESTION DES CLIENTS
# =====================================================

@router.get("/clients", response_model=List[ClientResponse])
def list_clients(
    db: Session = Depends(get_db),
    admin=Depends(require_admin)
):
    return Client.get_all(db)


@router.get("/clients/{client_id}", response_model=ClientResponse)
def get_client(
    client_id: int,
    db: Session = Depends(get_db),
    admin=Depends(require_admin)
):
    client = Client.get_by_id(db, client_id)
    if not client:
        raise HTTPException(404, "Client introuvable")
    return client


# =====================================================
# 🟦 SECTION 3 — GESTION DES DEMANDES
# =====================================================

@router.get("/demandes", response_model=List[DemandeResponse])
def list_demandes(
    db: Session = Depends(get_db),
    admin=Depends(require_admin)
):
    return Demande.get_all(db)


@router.get("/demandes/{demande_id}", response_model=DemandeResponse)
def get_demande(
    demande_id: int,
    db: Session = Depends(get_db),
    admin=Depends(require_admin)
):
    demande = Demande.get_by_id(db, demande_id)
    if not demande:
        raise HTTPException(404, "Demande introuvable")
    return demande


@router.put("/demandes/{demande_id}")
def update_demande_statut(
    demande_id: int,
    data: UpdateStatutRequest,
    db: Session = Depends(get_db),
    admin=Depends(require_admin)
):
    demande = Demande.update_statut(db, demande_id, data.statut)
    if not demande:
        raise HTTPException(404, "Demande introuvable")

    return {
        "message": "Statut de la demande mis à jour",
        "demande_id": demande.id,
        "statut": demande.statut
    }


# =====================================================
# 🟦 SECTION 4 — GESTION DES OFFRES
# =====================================================

@router.get("/offres", response_model=List[OffreResponse])
def list_offres(
    db: Session = Depends(get_db),
    admin=Depends(require_admin)
):
    return Offre.get_all(db)


@router.post("/offres", response_model=OffreResponse, status_code=status.HTTP_201_CREATED)
def create_offre(
    data: OffreRequest,
    db: Session = Depends(get_db),
    admin=Depends(require_admin)
):
    return Offre.create(db, **data.dict())


@router.put("/offres/{offre_id}", response_model=OffreResponse)
def update_offre(
    offre_id: int,
    data: UpdateOffreRequest,
    db: Session = Depends(get_db),
    admin=Depends(require_admin)
):
    offre = Offre.update(db, offre_id, **data.dict(exclude_unset=True))
    if not offre:
        raise HTTPException(404, "Offre introuvable")
    return offre


@router.delete("/offres/{offre_id}")
def delete_offre(
    offre_id: int,
    db: Session = Depends(get_db),
    admin=Depends(require_admin)
):
    if not Offre.delete(db, offre_id):
        raise HTTPException(404, "Offre introuvable")

    return {"message": "Offre supprimée"}


# =====================================================
# 🟦 SECTION 5 — GESTION DES CONTRATS
# =====================================================

@router.get("/contrats", response_model=List[ContratResponse])
def list_contrats(
    db: Session = Depends(get_db),
    admin=Depends(require_admin)
):
    return Contrat.get_all(db)


@router.post("/contrats", response_model=ContratResponse, status_code=status.HTTP_201_CREATED)
def create_contrat(
    data: CreateContratRequest,
    db: Session = Depends(get_db),
    admin=Depends(require_admin)
):
    return Contrat.create(
        db=db,
        client_id=data.client_id,
        offre_id=data.offre_id,
        date_debut=data.date_debut,
        date_fin=data.date_fin
    )


@router.put("/contrats/{contrat_id}")
def update_contrat_statut(
    contrat_id: int,
    data: UpdateContratStatutRequest,
    db: Session = Depends(get_db),
    admin=Depends(require_admin)
):
    contrat = Contrat.update_statut(db, contrat_id, data.statut)
    if not contrat:
        raise HTTPException(404, "Contrat introuvable")

    return {
        "message": "Statut du contrat mis à jour",
        "contrat_id": contrat.id,
        "statut": contrat.statut
    }

@router.delete("/contrats/{contrat_id}")
def delete_contrat(
    contrat_id: int,
    db: Session = Depends(get_db),
    admin=Depends(require_admin)
):
    if not Contrat.delete(db, contrat_id):
        raise HTTPException(
            status_code=404,
            detail="Contrat introuvable"
        )

    return {
        "message": "Contrat supprimé avec succès",
        "contrat_id": contrat_id
    }
