from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime
from sqlalchemy.sql import func
from sqlalchemy.orm import Session
from app.core.database import Base


class Demande(Base):
    __tablename__ = "demande"

    id = Column(Integer, primary_key=True, index=True)
    client_id = Column(Integer, ForeignKey("client.id"), nullable=False)
    message = Column(Text, nullable=False)
    type_demande = Column(String(50))
    statut = Column(String(50), default="EN_ATTENTE")
    date_creation = Column(DateTime(timezone=True), server_default=func.now())

    # ==================================================
    # 🔹 MÉTHODES MÉTIER (DATA ACCESS LAYER)
    # ==================================================

    @classmethod
    def get_all(cls, db: Session):
        """
        Récupérer toutes les demandes (ADMIN)
        """
        return db.query(cls).order_by(cls.date_creation.desc()).all()

    @classmethod
    def get_by_id(cls, db: Session, demande_id: int):
        """
        Récupérer une demande par ID
        """
        return db.query(cls).filter(cls.id == demande_id).first()

    @classmethod
    def get_by_client(cls, db: Session, client_id: int):
        """
        Récupérer toutes les demandes d'un client
        """
        return (
            db.query(cls)
            .filter(cls.client_id == client_id)
            .order_by(cls.date_creation.desc())
            .all()
        )

    @classmethod
    def create(cls, db: Session, client_id: int, message: str, type_demande: str):
        """
        Créer une nouvelle demande (CLIENT)
        """
        demande = cls(
            client_id=client_id,
            message=message,
            type_demande=type_demande,
            statut="EN_ATTENTE"
        )

        db.add(demande)
        db.commit()
        db.refresh(demande)
        return demande

    @classmethod
    def update_statut(cls, db: Session, demande_id: int, statut: str):
        """
        Mettre à jour le statut d'une demande (ADMIN / AGENT)
        """
        demande = cls.get_by_id(db, demande_id)

        if not demande:
            return None

        demande.statut = statut
        db.commit()
        db.refresh(demande)
        return demande
