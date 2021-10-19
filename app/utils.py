import time
from typing import Dict

import jwt

def token_response(token: str):
    return{
        'token_type': 'bearer',
        'access_token': token        
    }
    
JWT_SECRET = 'sadiouhiouhuiohewyr98syadf98ysdf98y'

def sign_jwt(user_id: str) ->Dict[str, str]:
    payload = {
        'user_id': user_id,
        'expires': time.time() + 2400
    }
    return token_response(jwt.encode(payload, JWT_SECRET, algorithm="HS256"))


def decodeJWT(token: str) -> dict:
    try:
        decoded_token = jwt.decode(
            token.encode(), JWT_SECRET, algorithms=["HS256"])
        return decoded_token if decoded_token['expires'] >= time.time() else None
    except:
        return {}
    

