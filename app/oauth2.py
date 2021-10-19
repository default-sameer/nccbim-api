from fastapi import status, HTTPException, Depends
from app.token import SECRET_KEY, ALGORITHM
from fastapi.security import OAuth2PasswordBearer
from app.token import verify_token
from app.models import User

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

async def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    
    verify_token(token, credentials_exception)
    
    
async def get_current_active_user(current_user: User = Depends(get_current_user)):
    if current_user.disabled():
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user
