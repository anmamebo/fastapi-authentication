from app.models.user import User
from app.schemas.user import UserIn
from app.utils.security import get_password_hash
from sqlmodel import Session, select


def get_user_by_username(db: Session, username: str):
    return db.exec(select(User).where(User.username == username)).first()


def get_user_by_email(db: Session, email: str):
    return db.exec(select(User).where(User.email == email)).first()


def create_user(db: Session, user: UserIn):
    hashed_password = get_password_hash(user.password)
    db_user = User(
        username=user.username,
        email=user.email,
        hashed_password=hashed_password,
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
