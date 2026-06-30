from jose import jwt
from jose import JWTError
from datetime import datetime,timedelta
from passlib.context import CryptContext
from sqlalchemy.util import deprecated_params

pwd_context=CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)
def create_hash_password(password:str):
    return pwd_context.hash(password)
def verfiy_password(password,hash_password):
    return pwd_context.verify(hash_password,password)
def create_token(data:dict):
    payload=data.copy()
    expire=datetime.utcnow()+timedelta(minutes=30)
    payload.update({
        "exp":expire
    })
    token=jwt.encode(
        payload,
        SECRET_KEY,
        algorithm=ALGORITHM
    )
    return token
def verify_token(token:str):
    try:
        payload=jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )
        return payload

    except JWTError:
        return None


