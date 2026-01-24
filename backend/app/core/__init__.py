from app.core.database import SessionLocal
from app.models.role import Role

def init_roles():
    db = SessionLocal()

    roles = ["CLIENT", "AGENT", "ADMIN"]

    for r in roles:
        exists = db.query(Role).filter(Role.nom == r).first()
        if not exists:
            db.add(Role(nom=r))

    db.commit()
    db.close()
