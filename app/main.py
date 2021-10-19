from fastapi import FastAPI, Depends
from app.routers import user, student, auth
from app.jwt_brearer import JWTBearer
from app.oauth2 import get_current_user

app = FastAPI()

# token_listener = get_current_user

@app.get('/', tags=['Root'])
def root():
    return {'Visit /docs for all API Endpoints.'}


app.include_router(auth.auth)
app.include_router(user.user)
# app.include_router(student.student, dependencies=[Depends(token_listener)])
app.include_router(student.student)



