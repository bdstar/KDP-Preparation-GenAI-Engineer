from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError
 
oauth2 = OAuth2PasswordBearer(tokenUrl="token")
 
def current_user(token: str = Depends(oauth2)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
    except JWTError:
        raise HTTPException(status_code=401, detail="invalid token")
    return payload["sub"]
