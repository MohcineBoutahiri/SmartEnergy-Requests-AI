from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime
from sqlalchemy.sql import func
from app.core.database import Base

class Demande(Base):
    __tablename__ = "demande"

    id = Column(Integer, primary_key=True, index=True)
    message = Column(Text)
    type_demande = Column(String)
    statut = Column(String, default="EN_ATTENTE")
    date_creation = Column(DateTime(timezone=True), server_default=func.now())
    client_id = Column(Integer, ForeignKey("client.id"))
