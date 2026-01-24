from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship, Session
from app.core.database import Base


class Utilisateur(Base):
    __tablename__ = "utilisateur"

    id = Column(Integer, primary_key=True, index=True)
    nom = Column(String(100))
    email = Column(String(100), unique=True, nullable=False)
    mot_de_passe = Column(String(255), nullable=False)
    actif = Column(Boolean, default=True)
    role_id = Column(Integer, ForeignKey("role.id"))

    client = relationship(
        "Client",
        back_populates="utilisateur",
        uselist=False
    )

    # ==================================================
    # 🔹 MÉTHODES MÉTIER — UTILISATEUR
    # ==================================================

    @classmethod
    def get_all(cls, db: Session):
        """Lister tous les utilisateurs (ADMIN)"""
        return db.query(cls).order_by(cls.id.desc()).all()

    @classmethod
    def get_by_id(cls, db: Session, user_id: int):
        """Récupérer un utilisateur par ID"""
        return db.query(cls).filter(cls.id == user_id).first()

    @classmethod
    def get_by_email(cls, db: Session, email: str):
        """Récupérer un utilisateur par email"""
        return db.query(cls).filter(cls.email == email).first()

    @classmethod
    def create(
        cls,
        db: Session,
        nom: str,
        email: str,
        mot_de_passe: str,
        role_id: int,
        actif: bool = True
    ):
        """Créer un utilisateur (ADMIN)"""
        user = cls(
            nom=nom,
            email=email,
            mot_de_passe=mot_de_passe,
            role_id=role_id,
            actif=actif
        )

        db.add(user)
        db.commit()
        db.refresh(user)
        return user

    @classmethod
    def update(
        cls,
        db: Session,
        user_id: int,
        nom: str | None = None,
        email: str | None = None,
        role_id: int | None = None,
        actif: bool | None = None
    ):
        """Modifier un utilisateur"""
        user = cls.get_by_id(db, user_id)

        if not user:
            return None

        if nom is not None:
            user.nom = nom
        if email is not None:
            user.email = email
        if role_id is not None:
            user.role_id = role_id
        if actif is not None:
            user.actif = actif

        db.commit()
        db.refresh(user)
        return user

    @classmethod
    def disable(cls, db: Session, user_id: int):
        """Désactiver un utilisateur"""
        return cls.update(db, user_id, actif=False)

    @classmethod
    def delete(cls, db: Session, user_id: int):
        """Supprimer un utilisateur"""
        user = cls.get_by_id(db, user_id)

        if not user:
            return False

        db.delete(user)
        db.commit()
        return True
