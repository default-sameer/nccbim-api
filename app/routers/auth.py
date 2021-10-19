from fastapi import APIRouter, Body, HTTPException, status, Depends
from fastapi.encoders import jsonable_encoder
from fastapi.security import OAuth2PasswordRequestForm
from app.database import user_collection, add_user
from passlib.context import CryptContext
from app.utils import sign_jwt
from app.models import User
from app.token import create_access_token, ACCESS_TOKEN_EXPIRE_MINUTES
from datetime import timedelta



auth = APIRouter(prefix='/auth', tags=['Authentication'])

hash_helper = CryptContext(schemes=["bcrypt"])


@auth.post('/login')
async def login(data: OAuth2PasswordRequestForm = Depends()):
    user = user_collection.find_one({"email": data.username}, {"_id": 0})
    if(user):
        password = hash_helper.verify(data.password, user['password'])
        if(password):
            if user['verified']:
                access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
                access_token = create_access_token(data={"sub": user['email']}, expires_delta=access_token_expires)
                return {'token_type': 'bearer','access_token': access_token}
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail='Please Verify your Email and provide NCC College Id Card to access this API')
        return "Incorrect email or password"
    return "Incorrect email or password"


# @auth.post('/register')
# async def register(user: User = Body(...)):
#     user_exists = user_collection.find_one({'email': user.email}, {'_id':0})
#     if(user_exists):
#         return 'Email Already exists'
#     user.password = hash_helper.encrypt(user.password)
#     new_user = await add_user(jsonable_encoder(user))
#     return new_user


# @auth.post('/login')
# async def login(data:  HTTPBasicCredentials = Body(...)):
#     user = user_collection.find_one({"email": data.username}, {"_id": 0})
#     if(user):
#         password = hash_helper.verify(data.password, user['password'])
#         if(password):
#             if user['verified']:
#                 return sign_jwt(data.username)
#             raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
#                             detail='Please Verify your Email and provide NCC College Id Card to access this API')
#         return "Incorrect email or password"
#     return "Incorrect email or password"


# @auth.post('/register')
# async def register(user: User = Body(...)):
#     user_exists = user_collection.find_one({'email': user.email}, {'_id':0})
#     if(user_exists):
#         return 'Email Already exists'
#     user.password = hash_helper.encrypt(user.password)
#     new_user = await add_user(jsonable_encoder(user))
#     return new_user
