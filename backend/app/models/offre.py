from sqlalchemy import Column, Integer, String, Boolean, Numeric
from sqlalchemy.orm import Session
from app.core.database import Base


class Offre(Base):
    __tablename__ = "offre"

    id = Column(Integer, primary_key=True, index=True)
    nom = Column(String(100), nullable=False)
    type_energie = Column(String(50), nullable=False)  # Gaz / Electricité / Duo
    prix_kwh = Column(Numeric(10, 4), nullable=False)
    duree_mois = Column(Integer, nullable=False)
    actif = Column(Boolean, default=True)

    # ==================================================
    # 🔹 MÉTHODES MÉTIER — OFFRE
    # ==================================================

    @classmethod
    def get_all(cls, db: Session):
        """Lister toutes les offres (ADMIN)"""
        return db.query(cls).order_by(cls.id.desc()).all()

    @classmethod
    def get_active(cls, db: Session):
        """Lister les offres actives (CLIENT)"""
        return db.query(cls).filter(cls.actif == True).all()

    @classmethod
    def get_by_id(cls, db: Session, offre_id: int):
        return db.query(cls).filter(cls.id == offre_id).first()

    @classmethod
    def create(
        cls,
        db: Session,
        nom: str,
        type_energie: str,
        prix_kwh: float,
        duree_mois: int
    ):
        offre = cls(
            nom=nom,
            type_energie=type_energie,
            prix_kwh=prix_kwh,
            duree_mois=duree_mois,
            actif=True
        )

        db.add(offre)
        db.commit()
        db.refresh(offre)
        return offre

    @classmethod
    def update(
        cls,
        db: Session,
        offre_id: int,
        nom: str | None = None,
        type_energie: str | None = None,
        prix_kwh: float | None = None,
        duree_mois: int | None = None,
        actif: bool | None = None
    ):
        offre = cls.get_by_id(db, offre_id)
        if not offre:
            return None

        if nom is not None:
            offre.nom = nom
        if type_energie is not None:
            offre.type_energie = type_energie
        if prix_kwh is not None:
            offre.prix_kwh = prix_kwh
        if duree_mois is not None:
            offre.duree_mois = duree_mois
        if actif is not None:
            offre.actif = actif

        db.commit()
        db.refresh(offre)
        return offre

    @classmethod
    def delete(cls, db: Session, offre_id: int):
        offre = cls.get_by_id(db, offre_id)
        if not offre:
            return False

        db.delete(offre)
        db.commit()
        return True
