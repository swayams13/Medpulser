from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import SessionLocal
from models import User
from auth.auth import hash_password, verify_password, create_token

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/signup")
def signup(email: str, password: str, db: Session = Depends(get_db)):
    user = User(email=email, password=hash_password(password), role="admin")
    db.add(user)
    db.commit()
    return {"msg": "User created"}


@router.post("/login")
def login(email: str, password: str, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == email).first()
    if not user or not verify_password(password, user.password):
        return {"error": "Invalid"}

    token = create_token({"user": email})
    return {"token": token}
