from fastapi import FastAPI
from app.core.database import Base, engine

# ⚠️ IMPORT DES MODELS AVANT TOUT
from app.models.role import Role
from app.models.utilisateur import Utilisateur

from app.controllers.admin_controller import router as admin_router
from app.controllers.auth_controller import router as auth_router
from app.controllers.client_controller import router as client_router

app = FastAPI(title="API Energie IA")

Base.metadata.create_all(bind=engine)


app.include_router(auth_router)
app.include_router(admin_router)
app.include_router(client_router)


