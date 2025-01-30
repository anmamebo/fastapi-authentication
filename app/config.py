from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    SECRET_KEY: str = "secretkey"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    RESET_PASSWORD_SECRET_KEY: str = "secretkey"
    RESET_PASSWORD_ALGORITHM: str = "HS256"
    RESET_PASSWORD_EXPIRE_MINUTES: int = 30

    DB_DATABASE: str = "test.db"

    EMAIL_USERNAME: str
    EMAIL_PASSWORD: str
    EMAIL_FROM: str
    EMAIL_PORT: int
    EMAIL_SERVER: str

    FRONTEND_URL: str = "http://localhost:3000"

    class Config:
        env_file = ".env"


settings = Settings()
