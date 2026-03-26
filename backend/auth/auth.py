from passlib.context import CryptContext
import jwt

SECRET = "secretkey"
pwd_context = CryptContext(schemes=["bcrypt"])


def hash_password(password):
    return pwd_context.hash(password)


def verify_password(password, hashed):
    return pwd_context.verify(password, hashed)


def create_token(data):
    return jwt.encode(data, SECRET, algorithm="HS256")
