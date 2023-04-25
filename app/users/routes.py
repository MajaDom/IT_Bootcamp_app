import hashlib

from fastapi import APIRouter, status, HTTPException, Body, Depends
from email_validator import validate_email, EmailNotValidError
from starlette.background import BackgroundTasks
from starlette.requests import Request
from starlette.responses import JSONResponse

from app.users.schemas import *
from app.users.controller import UserController
from app.users.controller import JWTBearer

user_router = APIRouter(prefix="/api/users", tags=["Users"])


@user_router.post("/registration",
                  summary="User Registration",
                  status_code=status.HTTP_201_CREATED,
                  dependencies=[Depends(JWTBearer(["super_user"]))])
def register(user: UserRegistrationSchema, worker: BackgroundTasks):
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


@user_router.patch("/email-verification", summary="User Verification", status_code=status.HTTP_200_OK)
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


@user_router.post("/login", summary="User Login", )
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


@user_router.patch("/reset-password",
                   summary="Reset user's password. User route.",
                   dependencies=[Depends(JWTBearer(["super_user", "regular_user"]))]
                   )
def reset_password(request: Request, email: str = Body(embed=True)):
    """
    Function is used to reset the password of a user.
    It takes in an email as a parameter and sends an email with instructions on how to reset their password.

    Param email:str: Specify the email address of the user that is requesting a password reset.
    Return: The response object.
    """
    user_email = request.cookies.get("user_email")
    if user_email != email:
        raise HTTPException(detail="Unrecognized email.", status_code=400)
    UserController.change_password(email)
    response = JSONResponse(content="Request granted. Instructions are sent to your email.", status_code=200)
    response.set_cookie(key="code", value="active", max_age=600)
    return response


@user_router.patch("/forget-password", summary="Ask for password change.")
def forget_password(email: str = Body(embed=True)):
    """
    Function is used to send a new ver.code to the user's email.
    It takes an email as input and sends information on user's email.

    Param email:str: Specify the email address of the user whose password is to be changed.
    Return: A response object.
    """
    UserController.change_password(email)
    response = JSONResponse(content="Request granted. Instructions are sent to your email.", status_code=200)
    response.set_cookie(key="code", value="active", max_age=600)
    return response


@user_router.patch("/reset-password-complete",
                   summary="Save new password. User route.",
                   status_code=status.HTTP_201_CREATED
                   )
def reset_password_complete(request: Request, reset: ChangePasswordSchema):
    """
    The reset_password_complete function is used to reset the password of a user.
    It takes as input the code generated by send_reset_password, and two strings:
    the old password and the new one. It checks if both passwords match, hashes them using SHA256,
    and then calls UserController's reset password method to change it.

    Param request:Request: Get the user's cookie.
    Param code:int: Identify the user.
    Param password:str: Set the new password for the user.
    Param new password:str: Set the new password for the user.
    Return: A response with a message that the reset password finished successfully.
    """
    if request.cookies.get("code") != "active":
        raise HTTPException(status_code=403, detail="Verification code expired. Ask for another one.")
    if reset.new_password != reset.repeat_password:
        raise HTTPException(status_code=400, detail="Passwords must match. Try again")
    password_hashed = hashlib.sha256(reset.new_password.encode()).hexdigest()
    UserController.reset_password_complete(reset.code, password_hashed)
    response = JSONResponse(content="Reset password finished successfully. You can login now.", status_code=200)
    response.delete_cookie(key="code")
    return response


@user_router.get("/logout", summary="Logout user.", status_code=status.HTTP_200_OK)
def logout(request: Request, response: JSONResponse):
    if request.cookies:
        response.delete_cookie(key="user_email")
        response.delete_cookie(key="user_id")
    return {"message": "success"}


@user_router.patch("/deactivation", summary="Deactivate user.", dependencies=[Depends(JWTBearer(["super_user"]))])
def deactivate_user(user_id: str = Body(embed=True)):
    """
    Function takes a user_id as an argument and deactivates the corresponding user.
    It returns True if the operation was successful, False otherwise.

    Param user_id:str: Specify the user that is to be deactivated
    Return: The user-controller.
    """
    return UserController.change_user_status(user_id, activity=False)


@user_router.patch("/activation", summary="Deactivate user.", dependencies=[Depends(JWTBearer(["super_user"]))])
def deactivate_user(user_id: str = Body(embed=True)):
    """
    Function takes a user_id as an argument and deactivates the corresponding user.
    It returns True if the operation was successful, False otherwise.

    Param user_id:str: Specify the user that is to be deactivated
    Return: The user-controller.
    """
    return UserController.change_user_status(user_id, activity=True)


@user_router.get("/", summary="Get all users.", dependencies=[Depends(JWTBearer(["super_user"]))])
def get_all_users():
    return UserController.get_all_users()


@user_router.put("/",
                 summary="Edit user.",
                 dependencies=[Depends(JWTBearer(["regular_user", "super_user"]))],
                 response_model=UserSchema)
def edit_user(request: Request, user: UserUpdateSchema):
    user_id = request.cookies.get("user_id")
    user_dict = {attr: value for attr, value in user.dict().items() if value}
    return UserController.edit_user(user_id, user_dict)
