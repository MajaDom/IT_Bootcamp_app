"""User Service module"""
import hashlib

from fastapi import BackgroundTasks
from starlette.responses import JSONResponse

from app.users.repositories import UserRepository
from app.db.database import SessionLocal
from app.users.models import User
from app.users.exceptions import *
from .mail_service import EmailServices
from app.utils import generate_random_int, validate_password


class UserServices:
    """Service for User routes."""
    @staticmethod
    def create_new_user(worker: BackgroundTasks, first_name: str, last_name: str, email: str, password: str):
        """
        The create_new_user function creates a new user in the database.
        It takes as input an email, password, username and verification code.
        The function returns the newly created user.

        Param email:str: Store the email of the user.
        Param password:str: Hash the password.
        Param first_name:str: First name.
        Param last_name:str: Last name.
        Return: The user object that was created.
        """
        try:
            code = generate_random_int()
            if not validate_password(password):
                raise InvalidPasswordForm
            password = hashlib.sha256(password.encode()).hexdigest()
            with SessionLocal() as db:
                repository = UserRepository(db, User)
                fields = {"first_name": first_name, "last_name": last_name, "email": email, "password_hashed": password, "verification_code": code}
                obj = repository.create(fields)
            worker.add_task(EmailServices.send_code_for_verification, obj.email, code, first_name)
            return JSONResponse(
                content="Finish your registration. Instructions are sent to your email.",
                status_code=200
            )
        except Exception as exc:
            raise exc

    @staticmethod
    def verify_user(verification_code: int):
        """
        Function is used to verify a user's email address.
        It takes in a verification code and checks the database for that code.
        If it exists, it updates the user's verification_code field to None.

        Param verification_code:int: Pass the verification code to the function
        Return: The user object.
        """
        try:
            with SessionLocal() as db:
                repository = UserRepository(db, User)
                user = repository.read_user_by_code(verification_code)
                if user:
                    obj = repository.update(user, {"verification_code": None})
                return obj
        except Exception as exc:
            raise exc

    @staticmethod
    def login_user(email: str, password: str):
        """
        Function is used to authenticate a user by checking the email and password
        provided. If the credentials are valid, then it returns an object of type User.


        Param email:str: Pass the email address of the user logging in
        Param password:str: Store the password entered by the user
        Return: The user object.
        """
        try:
            with SessionLocal() as db:
                repository = UserRepository(db, User)
                user = repository.read_user_by_email(email)
                if not user or user.password_hashed != password:
                    raise InvalidCredentialsException
                if user.verification_code is not None:
                    raise UnverifiedAccountException
                if not user.is_active:
                    raise InactiveUserException
                return user
        except Exception as exc:
            raise exc
