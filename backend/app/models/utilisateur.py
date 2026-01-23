from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from app.core.database import Base

class Utilisateur(Base):
    __tablename__ = "utilisateur"

    id = Column(Integer, primary_key=True, index=True)
    nom = Column(String(100))
    email = Column(String(100), unique=True, index=True)
    mot_de_passe = Column(String(255))
    actif = Column(Boolean, default=True)

    role_id = Column(Integer, ForeignKey("role.id"), nullable=False)
