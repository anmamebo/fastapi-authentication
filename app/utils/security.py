from datetime import datetime, timedelta

import jwt
from app.config import settings
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def get_password_hash(password: str):
    """Hash the password using bcrypt."""
    return pwd_context.hash(password)


def verify_password(plain_password: str, hashed_password: str):
    """Verify the password using bcrypt."""
    return pwd_context.verify(plain_password, hashed_password)


def create_access_token(data: dict, expires_delta: timedelta | None = None):
    """Create an access token using the data provided."""
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now() + expires_delta
    else:
        expire = datetime.now() + timedelta(
            minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES
        )
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(
        to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM
    )
    return encoded_jwt


def decode_access_token(token: str):
    """Decode the access token."""
    try:
        payload = jwt.decode(
            token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM]
        )
        return payload
    except jwt.ExpiredSignatureError:
        return None


def generate_password_reset_token(email: str):
    """Generate a password reset token."""
    expire = datetime.now() + timedelta(minutes=settings.RESET_PASSWORD_EXPIRE_MINUTES)
    payload = {"sub": email, "exp": expire}
    return jwt.encode(
        payload,
        settings.RESET_PASSWORD_SECRET_KEY,
        algorithm=settings.RESET_PASSWORD_ALGORITHM,
    )


def decode_password_reset_token(token: str):
    """Decode the password reset token."""
    try:
        payload = jwt.decode(
            token,
            settings.RESET_PASSWORD_SECRET_KEY,
            algorithms=[settings.RESET_PASSWORD_ALGORITHM],
        )
        return payload.get("sub")  # Devuelve el email
    except jwt.ExpiredSignatureError:
        return None
