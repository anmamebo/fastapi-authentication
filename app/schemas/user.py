from pydantic import BaseModel, EmailStr


class UserBase(BaseModel):
    username: str
    email: EmailStr


class UserIn(UserBase):
    password: str


class UserOut(UserBase):
    id: int

    class Config:
        from_attributes = (
            True  # Permite la conversión de objetos ORM a modelos Pydantic
        )


class UserInDB(UserBase):
    hashed_password: str


class Token(BaseModel):
    access_token: str
    token_type: str
    # user: UserResponse


class ChangePasswordRequest(BaseModel):
    old_password: str
    new_password: str


class ForgotPasswordRequest(BaseModel):
    email: EmailStr


class ResetPasswordRequest(BaseModel):
    token: str
    new_password: str
