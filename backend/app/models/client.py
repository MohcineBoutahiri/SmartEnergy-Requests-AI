from sqlalchemy import Column, Integer, String, ForeignKey
from app.core.database import Base

class Client(Base):
    __tablename__ = "client"

    id = Column(Integer, primary_key=True, index=True)
    telephone = Column(String)
    adresse = Column(String)
    utilisateur_id = Column(Integer, ForeignKey("utilisateur.id"))
