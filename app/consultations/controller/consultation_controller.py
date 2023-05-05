"""User Controller module"""
import datetime

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
            return ConsultationService.create_new_consultation(topic=topic, description=description, user_id=user_id)
        except AppException as exc:
            raise HTTPException(status_code=exc.code, detail=exc.message) from exc
        except Exception as exc:
            raise HTTPException(status_code=500, detail=str(exc)) from exc

    @staticmethod
    def read_all_consultations():
        try:
            return ConsultationService.read_all_consultations()
        except AppException as exc:
            raise HTTPException(status_code=exc.code, detail=exc.message) from exc
        except Exception as exc:
            raise HTTPException(status_code=500, detail=str(exc)) from exc

    @staticmethod
    def read_consultation(consultation_id: int):
        try:
            return ConsultationService.read_consultation(consultation_id=consultation_id)
        except AppException as exc:
            raise HTTPException(status_code=exc.code, detail=exc.message) from exc
        except Exception as exc:
            raise HTTPException(status_code=500, detail=str(exc)) from exc

    @staticmethod
    def update_consultation(consultation_id: int, updates: dict, request: Request):
        try:
            if "status" in updates and updates["status"]:
                updates["date_confirmed"] = datetime.datetime.now()
                confirmed_by = get_jwt_token(request=request)["user_id"]
                updates["confirmed_by"] = confirmed_by
            return ConsultationService.update_consultation(consultation_id=consultation_id, updates=updates)
        except AppException as exc:
            raise HTTPException(status_code=exc.code, detail=exc.message) from exc
        except Exception as exc:
            raise HTTPException(status_code=500, detail=str(exc)) from exc

    @staticmethod
    def delete_consultation(consultation_id: int):
        try:
            return ConsultationService.delete_consultation(consultation_id=consultation_id)
        except AppException as exc:
            raise HTTPException(status_code=exc.code, detail=exc.message) from exc
        except Exception as exc:
            raise HTTPException(status_code=500, detail=str(exc)) from exc

