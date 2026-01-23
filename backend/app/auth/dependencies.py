from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError
from app.auth.jwt import decode_token

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        payload = decode_token(token)
        return payload
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token invalide"
        )

def require_role(role: str):
    def role_checker(user=Depends(get_current_user)):
        if user.get("role") != role:
            raise HTTPException(
                status_code=403,
                detail="Accès interdit"
            )
        return user
    return role_checker
