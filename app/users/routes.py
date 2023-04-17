import hashlib

from fastapi import APIRouter, status, HTTPException, Body
from email_validator import validate_email, EmailNotValidError
from starlette.background import BackgroundTasks
from starlette.responses import JSONResponse

from app.users.schemas import UserSchemaIn, UserLoginSchema
from app.users.controller import UserController

user_router = APIRouter(prefix="/api/users", tags=["Users"])


@user_router.post("/register",
                  summary="User Registration",
                  status_code=status.HTTP_201_CREATED
                  )
def register(user: UserSchemaIn, worker: BackgroundTasks):
    """
    Function creates a new user in the database.
    It takes as input a UserSchemaIn object, which is validated and converted to an equivalent UserSchemaOut object.
    The password is hashed using SHA256 before being stored in the database.

    Param user:UserSchemaIn: Tell the function that it will be receiving a user object.
    Return: A dictionary with the user's ID and token.
    """
    try:
        valid = validate_email(user.email)
        valid_email = valid.email
    except EmailNotValidError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc
    return UserController.create_user(worker, user.first_name, user.last_name, valid_email, user.password)


@user_router.patch("/user-verification",
                   summary="User Verification",
                   status_code=status.HTTP_200_OK
                   )
def verify_user(verification_code: int = Body(embed=True)):
    """
    Function verifies a user's account by verifying the verification code sent to their email.
    The function returns a response with the content 'Account verified. You can log in now' and status code 200 if
    the verification is successful, or it returns an error message and status code 400 if not.

    Param verification_code:int: Verify the user's account.
    Return: A response object.
    """
    UserController.verify_user(verification_code)
    return JSONResponse(content="Account verified. You can log in now", status_code=200)


@user_router.post("/user-login",
                  summary="User Login",
                  )
def login_user(login: UserLoginSchema, response: JSONResponse):
    """
    Function takes in a username, email, password and response object.
    It hashes the password using sha256 and then uses the UserController to login user.
    The function returns a token for the user.

    Param email:str: Check if the user exists in the database.
    Param password:str: Store the hashed password.
    Param response:Response: Set the cookie for the user.
    Return: The token and user_id of the logged-in user.
    """
    password_hashed = hashlib.sha256(login.password.encode()).hexdigest()
    token, user_id = UserController.login_user(login.email, password_hashed)
    response.set_cookie(key="user_id", value=user_id)
    response.set_cookie(key="user_email", value=login.email)
    return token
