"""User Repository module"""
from sqlalchemy.exc import IntegrityError

from app.base import BaseCRUDRepository, AppException
from app.users.models import User
from app.users.exceptions import InvalidVerificationCode


class UserRepository(BaseCRUDRepository):
    """Repository for User Model"""
    def create(self, attributes: dict):
        """
        The create function creates a new user in the database.
        It takes an attributes dictionary as its only parameter, and returns the created User object.
        If a user with this email already exists, it raises an AppException with code 400.

        Param attributes:dict: Pass in the attributes that are being passed into the create function.
        Return: The created object.
        """
        try:
            return super().create(attributes)
        except IntegrityError as exc:
            self.db.rollback()
            raise AppException(message="User with this email is already registered.", code=400) from exc

    def read_user_by_code(self, verification_code: int):
        """
        Function takes a verification code as an argument and returns the user object associated with that
        verification code. If no such user exists, it raises an InvalidVerificationCode exception.

        Param verification_code:int: Find the user with that verification code.
        Return: A user object if the verification code is valid.
        """
        try:
            user = self.db.query(User).filter(User.verification_code == verification_code).first()
            if not user:
                self.db.rollback()
                raise InvalidVerificationCode
            return user
        except Exception as exc:
            self.db.rollback()
            raise exc

    def read_user_by_email(self, email: str):
        """
        Function takes an email address as a string and returns the user object associated with that email.
        If no user is found, it raises an InvalidCredentialsException.

        Param email:str: Query the database for a user with that email address.
        Return: A user object.
        """
        try:
            return self.db.query(User).filter(User.email == email).first()
        except Exception as exc:
            self.db.rollback()
            raise exc

    def read_all_active_users(self, active=True):
        """
        The read_all_active_users function returns all active users in the database. If active param is False
        returns all inactive users.

        Param active=True: Filter the users to only return active users.
        Return: A list of users that are active.
        """
        try:
            users = self.db.query(User).filter(User.is_active == active).all()
            return users
        except Exception as exc:
            self.db.rollback()
            raise exc



