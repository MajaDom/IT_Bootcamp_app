"""User Controller module"""
from fastapi import HTTPException


from app.base.base_exception import AppException
from app.consultations.service import ConsultationService


class ConsultationController:
    """Controller for Consultation routes"""
    @staticmethod
    def create_new_consultation(topic: str, description: str, user_id: str):
        """

        """
        try:
            return ConsultationService.create_new_consultation(topic=topic, description=description, user_id=user_id)
        except AppException as exc:
            raise HTTPException(status_code=exc.code, detail=exc.message) from exc
        except Exception as exc:
            raise HTTPException(status_code=500, detail=str(exc)) from exc
