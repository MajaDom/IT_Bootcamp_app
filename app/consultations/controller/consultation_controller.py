"""User Controller module"""
from fastapi import HTTPException
from starlette.requests import Request

from app.base.base_exception import AppException
from app.consultations.service import ConsultationService
from app.users.service.user_auth_service import get_jwt_token


class ConsultationController:
    """Controller for Consultation routes"""
    @staticmethod
    def create_new_consultation(topic: str, description: str, request: Request):
        """

        """
        try:
            user_id = get_jwt_token(request=request)["user_id"]
            print("ovo je id: ", user_id)
            return ConsultationService.create_new_consultation(topic=topic, description=description, user_id=user_id)
        except AppException as exc:
            raise HTTPException(status_code=exc.code, detail=exc.message) from exc
        except Exception as exc:
            raise HTTPException(status_code=500, detail=str(exc)) from exc
