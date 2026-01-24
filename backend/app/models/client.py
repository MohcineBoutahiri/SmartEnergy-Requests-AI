from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, Session
from app.core.database import Base


class Client(Base):
    __tablename__ = "client"

    id = Column(Integer, primary_key=True, index=True)
    telephone = Column(String)
    adresse = Column(String)
    utilisateur_id = Column(Integer, ForeignKey("utilisateur.id"), unique=True)

    utilisateur = relationship(
        "Utilisateur",
        back_populates="client"
    )

    # ==================================================
    # 🔹 MÉTHODES MÉTIER — CLIENT
    # ==================================================

    @classmethod
    def get_all(cls, db: Session):
        """Lister tous les clients (ADMIN)"""
        return db.query(cls).order_by(cls.id.desc()).all()

    @classmethod
    def get_by_id(cls, db: Session, client_id: int):
        """Récupérer un client par ID"""
        return db.query(cls).filter(cls.id == client_id).first()

    @classmethod
    def get_by_user(cls, db: Session, utilisateur_id: int):
        """Récupérer le client lié à un utilisateur"""
        return db.query(cls).filter(
            cls.utilisateur_id == utilisateur_id
        ).first()

    @classmethod
    def create(cls, db: Session, utilisateur_id: int):
        """
        Créer automatiquement un client
        (appelé après /auth/register)
        """
        client = cls(
            utilisateur_id=utilisateur_id
        )

        db.add(client)
        db.commit()
        db.refresh(client)
        return client

    @classmethod
    def update_infos(
        cls,
        db: Session,
        utilisateur_id: int,
        telephone: str | None = None,
        adresse: str | None = None
    ):
        """
        Mettre à jour les informations personnelles du client
        """
        client = cls.get_by_user(db, utilisateur_id)

        if not client:
            return None

        if telephone is not None:
            client.telephone = telephone
        if adresse is not None:
            client.adresse = adresse

        db.commit()
        db.refresh(client)
        return client

    @classmethod
    def delete(cls, db: Session, client_id: int):
        """Supprimer un client (ADMIN)"""
        client = cls.get_by_id(db, client_id)

        if not client:
            return False

        db.delete(client)
        db.commit()
        return True
