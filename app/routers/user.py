from fastapi import APIRouter, Depends
from app.models import User
# from app.oauth2 import get_current_active_user

user = APIRouter(prefix='/user', tags=['Users'])

# @user.get('/me', response_model=User)
# async def read_users_me(current_user: User = Depends(get_current_active_user)):
#     return current_user
