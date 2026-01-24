from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from app.core.database import get_db
from app.auth.dependencies import get_current_user
from app.models.client import Client
from app.models.demande import Demande
from app.schemas.client_schema import UpdateClientRequest, ClientResponse
from app.schemas.demande_schema import CreateDemandeRequest, DemandeResponse

router = APIRouter(prefix="/client", tags=["Client"])

@router.put("/infos", response_model=ClientResponse)
def update_infos(
    data: UpdateClientRequest,
    db: Session = Depends(get_db),
    user=Depends(get_current_user)
):
    try:
        client = Client.update_infos(
            db=db,
            utilisateur_id=user["user_id"],
            telephone=data.telephone,
            adresse=data.adresse
        )

        if not client:
            raise HTTPException(404, "Client introuvable")

        return client

    except HTTPException:
        raise
    except Exception as e:
        print("❌ CLIENT UPDATE INFOS:", e)
        raise HTTPException(500, "Erreur interne")

@router.post("/demandes", response_model=DemandeResponse, status_code=status.HTTP_201_CREATED)
def create_demande(
    data: CreateDemandeRequest,
    db: Session = Depends(get_db),
    user=Depends(get_current_user)
):
    try:
        client = Client.get_by_user(db, user["user_id"])
        if not client:
            raise HTTPException(404, "Client introuvable")

        return Demande.create(
            db=db,
            client_id=client.id,
            message=data.message,
            type_demande=data.type_demande
        )

    except HTTPException:
        raise
    except Exception as e:
        print("❌ CLIENT CREATE DEMANDE:", e)
        raise HTTPException(500, "Erreur interne")

@router.get("/demandes", response_model=List[DemandeResponse])
def my_demandes(
    db: Session = Depends(get_db),
    user=Depends(get_current_user)
):
    try:
        client = Client.get_by_user(db, user["user_id"])
        if not client:
            raise HTTPException(404, "Client introuvable")

        return Demande.get_by_client(db, client.id)

    except HTTPException:
        raise
    except Exception as e:
        print("❌ CLIENT LIST DEMANDES:", e)
        raise HTTPException(500, "Erreur interne")

