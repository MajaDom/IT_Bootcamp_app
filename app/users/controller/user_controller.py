"""User Controller module"""
from fastapi import HTTPException


from app.base.base_exception import AppException
from app.users.service import UserServices
from app.users.exceptions import AdminLoginException
from app.users.service.user_auth_service import sign_jwt


class UserController:
    """Controller for User routes"""
    @staticmethod
    def create_user(worker, first_name, last_name, email, password):
        """
        Function creates a new user in the database.
        It takes as input an email, password and username. It returns a response with
        status code 200 if the creation was successful, or 400 if not.

        Param email: Receive the email address of the user
        Param password: Store the password of the user
        Param first_name: First name.
        Param last_name: Last name.
        Return: A response object.
        """
        try:
            return UserServices.create_new_user(worker, first_name, last_name, email, password)
        except AppException as exc:
            raise HTTPException(status_code=exc.code, detail=exc.message) from exc
        except Exception as exc:
            raise HTTPException(status_code=500, detail=str(exc)) from exc

    @staticmethod
    def verify_user(verification_code: int):
        """
        Function is used to verify a user's email address.
        It takes in an integer as a verification code and returns
        the user object associated with that code.

        Param verification_code:int: Verify the user.
        Return: A user object.
        """
        try:
            user = UserServices.verify_user(verification_code)
            return user
        except AppException as exc:
            raise HTTPException(status_code=exc.code, detail=exc.message) from exc
        except Exception as exc:
            raise HTTPException(status_code=500, detail=str(exc)) from exc

    @staticmethod
    def login_user(email: str, password: str):
        """
        Function is used to authenticate a user.
        It takes in an email and password as parameters, and returns a JWT token if the login is successful.
        If the login fails, it raises an HTTPException with status code 400 (Bad Request).

        Param email:str: Identify the user
        Param password:str: Check if the password is correct
        Return: A tuple containing the jwt, and the user's ID.
        """
        try:
            user = UserServices.login_user(email, password)
            if user.is_superuser:
                raise AdminLoginException(code=400, message="Use admin login.")
            return sign_jwt(user.id, "regular_user"), user.id

        except AppException as exc:
            raise HTTPException(status_code=exc.code, detail=exc.message, headers=exc.headers) from exc
        except Exception as exc:
            raise HTTPException(status_code=500, detail=str(exc)) from exc
