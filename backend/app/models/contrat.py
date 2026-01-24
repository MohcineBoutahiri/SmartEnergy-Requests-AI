from sqlalchemy import Column, Integer, String, Date, ForeignKey, DateTime
from sqlalchemy.sql import func
from sqlalchemy.orm import Session
from datetime import date
import uuid

from app.core.database import Base


class Contrat(Base):
    __tablename__ = "contrat"

    id = Column(Integer, primary_key=True, index=True)
    reference = Column(String(50), unique=True, nullable=False)
    client_id = Column(Integer, ForeignKey("client.id"), nullable=False)
    offre_id = Column(Integer, ForeignKey("offre.id"), nullable=False)
    date_debut = Column(Date, nullable=False)
    date_fin = Column(Date, nullable=False)
    statut = Column(String(50), default="GENERE")
    date_creation = Column(DateTime, server_default=func.now())

    # ==================================================
    # 🔹 MÉTHODES MÉTIER — CONTRAT
    # ==================================================

    @classmethod
    def generate_reference(cls):
        return f"CTR-{uuid.uuid4().hex[:8].upper()}"

    @classmethod
    def get_all(cls, db: Session):
        return db.query(cls).order_by(cls.date_creation.desc()).all()

    @classmethod
    def get_by_id(cls, db: Session, contrat_id: int):
        return db.query(cls).filter(cls.id == contrat_id).first()

    @classmethod
    def get_by_client(cls, db: Session, client_id: int):
        return db.query(cls).filter(
            cls.client_id == client_id
        ).all()

    @classmethod
    def create(
        cls,
        db: Session,
        client_id: int,
        offre_id: int,
        date_debut: date,
        date_fin: date
    ):
        contrat = cls(
            reference=cls.generate_reference(),
            client_id=client_id,
            offre_id=offre_id,
            date_debut=date_debut,
            date_fin=date_fin,
            statut="GENERE"
        )

        db.add(contrat)
        db.commit()
        db.refresh(contrat)
        return contrat

    @classmethod
    def update_statut(cls, db: Session, contrat_id: int, statut: str):
        contrat = cls.get_by_id(db, contrat_id)
        if not contrat:
            return None

        contrat.statut = statut
        db.commit()
        db.refresh(contrat)
        return contrat

    @classmethod
    def delete(cls, db: Session, contrat_id: int) -> bool:
        contrat = db.query(cls).filter(cls.id == contrat_id).first()
        if not contrat:
            return False

        db.delete(contrat)
        db.commit()
        return True