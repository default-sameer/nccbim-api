from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class Student(BaseModel):
    batch: int
    name: str
    # email: EmailStr
    tu_roll:str
    tu_registration: str
    # address: str
    
    class Config:
        orm_mode = True
    def hashing():
        pass
        
class User(BaseModel):
    username : str = Field(...)
    email: EmailStr = Field(...)
    password: str = Field(...)
    verified: Optional[bool] = False
    role: str = 'user'
    # disabled: Optional[bool] = None
    
    class Config:
        schema_extra = {
            "example": {
                "username": "username",
                "email": "email",
                "password": "password"
            }
        }
        

class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: Optional[str] = None
