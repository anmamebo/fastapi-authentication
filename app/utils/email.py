from app.config import settings
from fastapi import HTTPException, status
from fastapi_mail import ConnectionConfig, FastMail, MessageSchema

conf = ConnectionConfig(
    MAIL_USERNAME=settings.EMAIL_USERNAME,
    MAIL_PASSWORD=settings.EMAIL_PASSWORD,
    MAIL_FROM=settings.EMAIL_FROM,
    MAIL_PORT=settings.EMAIL_PORT,
    MAIL_SERVER=settings.EMAIL_SERVER,
    MAIL_STARTTLS=True,  # Usar STARTTLS
    MAIL_SSL_TLS=False,  # No usar SSL/TLS
    USE_CREDENTIALS=True,
    VALIDATE_CERTS=True,
)


async def send_reset_password_email(email: str, reset_token: str):
    """Send a password reset email."""
    reset_url = f"{settings.FRONTEND_URL}/reset-password?token={reset_token}"
    message = MessageSchema(
        subject="Restablecer contraseña",
        recipients=[email],
        body=f"Haz clic en el siguiente enlace para restablecer tu contraseña: {reset_url}",
        subtype="html",  # Opcional: para enviar el correo en formato HTML
    )
    fm = FastMail(conf)
    try:
        await fm.send_message(message)
    except Exception as e:
        print(f"Error al enviar el correo: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Error al enviar el correo de restablecimiento.",
        )
