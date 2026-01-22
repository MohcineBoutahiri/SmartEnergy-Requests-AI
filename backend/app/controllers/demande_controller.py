from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.models.demande import Demande
from app.schemas.demande_schema import DemandeCreate

router = APIRouter(prefix="/demandes", tags=["Demandes"])

@router.post("/")
def creer_demande(demande: DemandeCreate, db: Session = Depends(get_db)):
    new_demande = Demande(
        message=demande.message,
        client_id=demande.client_id
    )
    db.add(new_demande)
    db.commit()
    db.refresh(new_demande)
    return new_demande
