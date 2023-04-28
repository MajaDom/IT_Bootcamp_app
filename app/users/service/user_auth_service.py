"""User Authentication module"""
import time
from typing import Dict
import jwt

from app.config import settings
from app.users.exceptions import InvalidTokenException
from starlette.requests import Request

USER_SECRET = settings.USER_SECRET
JWT_ALGORITHM = settings.ALGORITHM
TOKEN_DURATION_SECONDS = settings.TOKEN_DURATION_SECONDS


def sign_jwt(user_id: str, role: str) -> Dict[str, str]:
    """
    Creates and returns user's access token.
    Param user_id: user's ID
    Param role: permission
    Return: token, dictionary.
    """
    payload = {
        "user_id": user_id,
        "role": role,
        "expires": time.time() + TOKEN_DURATION_SECONDS
    }
    token = jwt.encode(payload, USER_SECRET, algorithm=JWT_ALGORITHM)

    return {"access_token": token}


def decode_jwt(token: str) -> dict:
    """
    Decoding of access token.
    Param token: token string.
    Return: decoded token, dictionary.
    """

    try:
        decoded_token = jwt.decode(token, USER_SECRET, algorithms=[JWT_ALGORITHM])
        return decoded_token if decoded_token["expires"] >= time.time() else None
    except (jwt.PyJWTError, jwt.InvalidTokenError) as exc:
        raise InvalidTokenException from exc


def get_jwt_token(request: Request) -> dict:
    """
    Extracts JWT token from authorization header in request.
    Raises InvalidTokenError if token is invalid.
    """
    auth_headers = request.headers.get("Authorization")
    if not auth_headers:
        raise InvalidTokenException
    token = auth_headers.split(" ")[-1]
    try:
        decoded_token = decode_jwt(token)
    except InvalidTokenException as exc:
        raise InvalidTokenException from exc
    return decoded_token
