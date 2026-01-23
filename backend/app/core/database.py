from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker, declarative_base
from app.core.config import DATABASE_URL

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()

# ✅ TEST DE CONNEXION
try:
    with engine.connect() as connection:
        connection.execute(text("SELECT 1"))
        print("✅ Connexion PostgreSQL réussie")
except Exception as e:
    print("❌ Erreur de connexion PostgreSQL :", e)


# Dépendance FastAPI
def get_db():
    db = SessionLocal()
    try:
        print("📦 Session DB ouverte")
        yield db
    finally:
        db.close()
        print("📦 Session DB fermée")
