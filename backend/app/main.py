from fastapi import FastAPI
from app.controllers.demande_controller import router as demande_router

app = FastAPI(title="API Energie IA")

app.include_router(demande_router)
