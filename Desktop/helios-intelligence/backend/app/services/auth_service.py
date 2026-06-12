from sqlalchemy.orm import Session
from jose import jwt
from datetime import datetime, timedelta
from passlib.context import CryptContext

from app.models.user import User
from app.repositories.user_repository import UserRepository

pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)
SECRET_KEY = "helios-intelligence-jwt-secret-2026"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60


class AuthService:

    @staticmethod
    def register(
        db: Session,
        name: str,
        email: str,
        password: str
    ):

        existing_user = UserRepository.get_by_email(
            db=db,
            email=email
        )

        if existing_user:
            return {
                "error": "Email already registered"
            }

        hashed_password = pwd_context.hash(
            password
        )

        user = User(
            name=name,
            email=email,
            hashed_password=hashed_password
        )

        created_user = UserRepository.create(
            db=db,
            user=user
        )

        return {
            "id": created_user.id,
            "name": created_user.name,
            "email": created_user.email,
            "message": "User registered successfully"
        }
    
    @staticmethod
    def login(
        db: Session,
        email: str,
        password: str
    ):
        user = UserRepository.get_by_email(
            db=db,
            email=email
        )

        if not user:
            return {
                "error": "Invalid credentials"
            }

        if not pwd_context.verify(
            password,
            user.hashed_password
        ):
            return {
                "error": "Invalid credentials"
            }

        expire = datetime.utcnow() + timedelta(
            minutes=ACCESS_TOKEN_EXPIRE_MINUTES
        )

        token = jwt.encode(
            {
                "sub": user.email,
                "exp": expire
            },
            SECRET_KEY,
            algorithm=ALGORITHM
        )

        return {
            "access_token": token,
            "token_type": "bearer",
            "user": {
                "name": user.name,
                "email": user.email
            }
        }