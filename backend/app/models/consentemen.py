from sqlalchemy import Boolean, Column, Integer, String, Text, ForeignKey, DateTime
from sqlalchemy.sql import func
from app.core.database import Base



class Consentement(Base):
    __tablename__ = "consentement"

    id = Column(Integer, primary_key=True)
    client_id = Column(Integer, ForeignKey("client.id"), unique=True)
    accepte = Column(Boolean, nullable=False)
    ip_client = Column(String)

