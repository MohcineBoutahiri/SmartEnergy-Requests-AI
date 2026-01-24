from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from jose import JWTError

from app.auth.jwt import decode_token

# ===============================
# SECURITY SCHEME (Swagger clean)
# ===============================
security = HTTPBearer()


# ===============================
# GET CURRENT USER FROM JWT
# ===============================
def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(security)
):
    """
    Récupère l'utilisateur courant à partir du token JWT
    """
    try:
        token = credentials.credentials
        payload = decode_token(token)

        # Vérifications minimales
        if "user_id" not in payload or "role" not in payload:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Token invalide"
            )

        return payload

    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token invalide ou expiré"
        )


# ===============================
# ROLE-BASED ACCESS CONTROL
# ===============================
def require_role(required_role_id: int):
    """
    Vérifie que l'utilisateur possède le rôle requis
    """
    def role_checker(user=Depends(get_current_user)):
        if user.get("role") != required_role_id:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Accès interdit"
            )
        return user
    return role_checker


# ===============================
# ROLE SHORTCUTS
# ===============================
require_client = require_role(1)   # CLIENT
require_agent  = require_role(2)   # AGENT
require_admin  = require_role(3)   # ADMIN
