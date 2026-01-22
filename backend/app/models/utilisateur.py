from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from app.core.database import Base

class Utilisateur(Base):
    __tablename__ = "utilisateur"

    id = Column(Integer, primary_key=True, index=True)
    nom = Column(String)
    email = Column(String, unique=True, index=True)
    mot_de_passe = Column(String)
    actif = Column(Boolean, default=True)
    role_id = Column(Integer, ForeignKey("role.id"))
