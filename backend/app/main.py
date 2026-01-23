from fastapi import FastAPI

from app.core.database import Base, engine

# ⚠️ IMPORT DES MODELS (OBLIGATOIRE)
from app.models.role import Role
from app.models.utilisateur import Utilisateur

from app.controllers.auth_controller import router as auth_router

app = FastAPI(title="API Energie IA")

# ⚠️ Création des tables (DEV uniquement)
Base.metadata.create_all(bind=engine)

app.include_router(auth_router)
