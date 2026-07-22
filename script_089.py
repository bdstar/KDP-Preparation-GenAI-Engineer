from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
import jwt                                            # JSON Web Token handling
 
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")   # OAuth2 bearer-token flow
 
async def current_user(token: str = Depends(oauth2_scheme)):
    try:
        claims = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])   # verify signature
        return claims["sub"]                          # the authenticated user's identity
    except jwt.PyJWTError:
        raise HTTPException(status_code=401, detail="Invalid or expired token")
