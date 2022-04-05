from fastapi import FastAPI, Depends
from app.routers import user, student, auth
from app.jwt_brearer import JWTBearer
from app.oauth2 import get_current_user

app = FastAPI()


@app.get('/', tags=['Root'])
def root():
    return {'Visit /docs for all API Endpoints.'}
@app.get('/hello', tags=['Root'])
def hello():
    return {'hello world'}

app.include_router(auth.auth)
app.include_router(user.user)

app.include_router(student.student)



