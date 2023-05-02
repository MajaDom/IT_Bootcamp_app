"""User Controller module"""
from fastapi import HTTPException


from app.base.base_exception import AppException
from app.users.service import UserServices
from app.users.service import sign_jwt


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
    def verify_user(verification_code: int, worker):
        """
        Function is used to verify a user's email address.
        It takes in an integer as a verification code and returns
        the user object associated with that code.

        Param verification_code:int: Verify the user.
        Return: A user object.
        """
        try:
            user = UserServices.verify_user(verification_code, worker)
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
                return sign_jwt(user.id, "super_user"), user.id
            elif user.is_employee:
                return sign_jwt(user.id, "employee"), user.id
            return sign_jwt(user.id, "student"), user.id

        except AppException as exc:
            raise HTTPException(status_code=exc.code, detail=exc.message, headers=exc.headers) from exc
        except Exception as exc:
            raise HTTPException(status_code=500, detail=str(exc)) from exc

    @staticmethod
    def change_password(email: str):
        """
        Function is used to change the password of a user.
        It takes in an email as a parameter and returns the verification code
        that was sent to the user's email address.

        Param email:str: Get the user by email.
        Return: A verification code.
        """
        try:
            return UserServices.change_password(email)
        except AppException as exc:
            raise HTTPException(status_code=exc.code, detail=exc.message) from exc
        except Exception as exc:
            raise HTTPException(status_code=500, detail=str(exc)) from exc

    @staticmethod
    def reset_password_complete(code: int, password_hashed: str):
        """
        The reset_password_complete function takes in a code and password hashed,
        and returns the user object associated with that code. If no user is found,
        it raises an HTTPException with status_code 404. If there is an error in
        the database query or if the password does not match the hashed version of
        the new password, it raises an HTTPException with status_code 400.

        Param code:int: Identify the user who is trying to reset their password
        Param password-hashed:str: Store the hashed password
        Return: The user object.
        """
        try:
            user = UserServices.reset_password_complete(code, password_hashed)
            return user
        except AppException as exc:
            raise HTTPException(status_code=exc.code, detail=exc.message) from exc
        except Exception as exc:
            raise HTTPException(status_code=500, detail=str(exc)) from exc

    @staticmethod
    def register_employee(user_id: str, activity: bool = True):
        """
        Function is used to register or unregister an employee.

        Param user_id: User's ID.
        Param activity: Set employee's status to True or False
        Return: user's object.
        """
        try:
            user = UserServices.register_employee(user_id, activity)
            return user
        except AppException as exc:
            raise HTTPException(status_code=exc.code, detail=exc.message) from exc
        except Exception as exc:
            raise HTTPException(status_code=500, detail=str(exc)) from exc


    @staticmethod
    def change_user_status(user_id: str, activity: bool = False):
        """
        Function is used to activate/deactivate a user.
        It takes in the user_id of the user that needs to be
        (de)activated and returns the updated User object.

        Param user_id:str: Identify the user
        Param activity:bool=False: Set user's status.
        Return: The user object that was (de)activated.
        """
        try:
            user = UserServices.change_user_status(user_id, activity)
            return user
        except AppException as exc:
            raise HTTPException(status_code=exc.code, detail=exc.message) from exc
        except Exception as exc:
            raise HTTPException(status_code=500, detail=str(exc)) from exc

    @staticmethod
    def get_all_users():
        try:
            users = UserServices.get_all_users()
            return users
        except AppException as exc:
            raise HTTPException(status_code=exc.code, detail=exc.message) from exc
        except Exception as exc:
            raise HTTPException(status_code=500, detail=str(exc)) from exc

    @staticmethod
    def get_user_by_id(user_id: str):
        try:
            user = UserServices.get_user_by_id(user_id)
            return user
        except AppException as exc:
            raise HTTPException(status_code=exc.code, detail=exc.message) from exc
        except Exception as exc:
            raise HTTPException(status_code=500, detail=str(exc)) from exc

    @staticmethod
    def edit_user(user_id: str, user: dict):
        try:
            user = UserServices.edit_user(user_id, user)
            return user
        except AppException as exc:
            raise HTTPException(status_code=exc.code, detail=exc.message) from exc
        except Exception as exc:
            raise HTTPException(status_code=500, detail=str(exc)) from exc

    @staticmethod
    def get_all_active_users(active=True):
        """
        The get_all_active_users function retrieves all active users from the database.
        It takes an optional parameter, active, which defaults to True. If it is set to False,
        it will retrieve all inactive users instead.

        Param active=True: Filter the users by their active status.
        Return: A list of users that are active.
        """
        try:
            users = UserServices.get_all_active_users(active=active)
            return users
        except AppException as exc:
            raise HTTPException(status_code=exc.code, detail=exc.message) from exc
        except Exception as exc:
            raise HTTPException(status_code=500, detail=str(exc)) from exc

