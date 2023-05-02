"""Mail Service module"""
import asyncio

from fastapi_mail import ConnectionConfig, MessageSchema, MessageType, FastMail
from pydantic import EmailStr

from app.config import settings
from app.email_templates.user_registration_template import html_first_part, html_second_part, html_third_part
from app.email_templates.password_reset_template import first_part, second_part
from app.email_templates.account_verified import start, end


class EmailServices:
    """Service for mail operations"""
    conf = ConnectionConfig(
        MAIL_USERNAME=settings.MAIL_USERNAME,
        MAIL_PASSWORD=settings.MAIL_PASSWORD,
        MAIL_PORT=settings.MAIL_PORT,
        MAIL_SERVER=settings.MAIL_SERVER,
        MAIL_FROM=settings.MAIL_FROM,
        MAIL_STARTTLS=True,
        MAIL_SSL_TLS=False
    )

    @staticmethod
    def send_code_for_verification(email: EmailStr, code: int, first_name: str, password: str):
        """
        Function sends a verification code to the user's email address.
        The function takes in an email and a code as parameters, and uses them to create an HTML message
        that contains the code. The function then sends this message via FastMail.

        Param email:EmailStr: Store the email address of the user
        Param code:int: Send the verification code to the user.
        Return: The message that was sent to the user.
        """
        html = html_first_part + f"Welcome {first_name}. " + html_second_part + f"<strong>{str(code)}</strong>"
        html += f"<p>Your password for login is: </p>{password}"
        html += "<p>Reset your password as soon as possible for security reasons</p>"
        html += html_third_part

        message = MessageSchema(
            subject="Finish your registration on ITBootcamp.",
            recipients=[email],
            body=html,
            subtype=MessageType.html,
        )
        fm = FastMail(EmailServices.conf)
        asyncio.run(fm.send_message(message))

    @staticmethod
    def send_code_for_password_reset(email: EmailStr, code: int):
        """
        Function sends a code to the user's email address.
        The function takes in an email and a code as parameters, and uses them to send the user
        an HTML message containing their password reset code.

        Param email:EmailStr: Specify the email address of the user who is requesting a password reset
        Param code:int: Send the code to the user.
        Return: A future object.
        """
        html = first_part + f"<strong>{str(code)}</strong>" + second_part
        message = MessageSchema(
            subject="Reset Password.",
            recipients=[email],
            body=html,
            subtype=MessageType.html,
        )
        fm = FastMail(EmailServices.conf)
        asyncio.run(fm.send_message(message))

    @staticmethod
    def send_confirmation(email: EmailStr, first_name: str):
        html = start + f"<h2>Hello {first_name},</h2>" + end
        message = MessageSchema(
            subject="Welcome.",
            recipients=[email],
            body=html,
            subtype=MessageType.html,
        )
        fm = FastMail(EmailServices.conf)
        asyncio.run(fm.send_message(message))
