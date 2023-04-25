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
            password_hashed = hashlib.sha256(password.encode()).hexdigest()
            with SessionLocal() as db:
                repository = UserRepository(db, User)
                fields = {
                    "first_name": first_name,
                    "last_name": last_name,
                    "email": email,
                    "password_hashed": password_hashed,
                    "verification_code": code
                }
                obj = repository.create(fields)
            worker.add_task(EmailServices.send_code_for_verification, obj.email, code, first_name, password)
            return JSONResponse(
                content="Registration successful. Instructions are sent to user`s email.",
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

    @staticmethod
    def change_password(email: str):
        """
        Function takes email parameter and after check, sets User for password change.

        Param email: str: email string
        Return: User object
        """
        try:
            with SessionLocal() as db:
                repository = UserRepository(db, User)
                user = repository.read_user_by_email(email)
                if not user:
                    raise UserEmailDoesNotExistsException(message=f"Email: {email} does not exist in our Database.")
                code = generate_random_int()
                obj = repository.update(user, {"verification_code": code})
                EmailServices.send_code_for_password_reset(user.email, code)
                return obj
        except Exception as exc:
            raise exc

    @staticmethod
    def reset_password_complete(code: int, password_hashed: str):
        """
        The reset_password_complete function takes in a code and password hashed,
        and updates the user's password to be the hashed version of the new password.

        Param code:int: Identify the user.
        Param password hashed:str: Store the hashed password, and the code:int parameter is used to store
        the verification code.
        Return: A dictionary with the key &quot;success&quot; and value true.
        """
        try:
            with SessionLocal() as db:
                repository = UserRepository(db, User)
                user = repository.read_user_by_code(code)
                updates = {"password_hashed": password_hashed, "verification_code": None}
                return repository.update(user, updates)
        except Exception as exc:
            raise exc

    @staticmethod
    def change_user_status(user_id: str, activity: bool = False):
        """
        The change_user_status function is used to change the status of a user.
        It takes two parameters, user_id and activity. If activity is True, then the user will be activated
        and if it is False, the user will be deactivated.

        Param user_id:str: Identify the user to be updated
        Param activity:bool=False: Set the activity status of a user
        Return: The updated user object.
        """
        try:
            with SessionLocal() as db:
                repository = UserRepository(db, User)
                user = UserServices.get_user_by_id(user_id)
                updates = {"is_active": activity}
                return repository.update(user, updates)
        except Exception as exc:
            raise exc

    @staticmethod
    def get_user_by_id(user_id: str):
        """
        Function is used to retrieve a user by their ID.
        It takes in the user_id as an argument and returns the User object associated with that ID.

        Param user_id:str: Pass the user_id to the function.
        Return: A user object.
        """
        try:
            with SessionLocal() as db:
                repository = UserRepository(db, User)
                return repository.read_by_id(user_id)
        except Exception as exc:
            raise exc

    @staticmethod
    def get_all_users():
        try:
            with SessionLocal() as db:
                repository = UserRepository(db, User)
                return repository.read_all()
        except Exception as exc:
            raise exc

    @staticmethod
    def edit_user(user_id: str, user: dict):
        try:
            with SessionLocal() as db:
                repository = UserRepository(db, User)
                user_object = repository.read_by_id(user_id)
                return repository.update(user_object, user)
        except Exception as exc:
            raise exc
