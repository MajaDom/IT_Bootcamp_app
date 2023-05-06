"""Participant controller module"""
import datetime

from fastapi import HTTPException
from starlette.requests import Request

from app.base.base_exception import AppException
from app.participants.services import ParticipantService
from app.users.service.user_auth_service import get_jwt_token


class ParticipantController:
    """Controller for Participant routes"""

    @staticmethod
    def create_new_participant(description: str, consultation_id: int, request: Request):
        """

        """
        try:
            user_id = get_jwt_token(request=request)["user_id"]
            return ParticipantService.create_new_participant(description=description, user_id=user_id,
                                                             consultation_id=consultation_id)
        except AppException as exc:
            raise HTTPException(status_code=exc.code, detail=exc.message) from exc
        except Exception as exc:
            raise HTTPException(status_code=500, detail=str(exc)) from exc

    @staticmethod
    def read_all_participants():
        try:
            return ParticipantService.read_all_participants()
        except AppException as exc:
            raise HTTPException(status_code=exc.code, detail=exc.message) from exc
        except Exception as exc:
            raise HTTPException(status_code=500, detail=str(exc)) from exc

    @staticmethod
    def read_participants_of_one_consultation(consultation_id: int):
        try:
            return ParticipantService.read_participants_of_one_consultation(consultation_id=consultation_id)
        except AppException as exc:
            raise HTTPException(status_code=exc.code, detail=exc.message) from exc
        except Exception as exc:
            raise HTTPException(status_code=500, detail=str(exc)) from exc

    @staticmethod
    def update_participant(participant_id: int, updates: dict, request: Request):
        try:

            user_id = get_jwt_token(request=request)["user_id"]
            updates["user_id"] = user_id
            return ParticipantService.update_participant(participant_id=participant_id, updates=updates)
        except AppException as exc:
            raise HTTPException(status_code=exc.code, detail=exc.message) from exc
        except Exception as exc:
            raise HTTPException(status_code=500, detail=str(exc)) from exc

    @staticmethod
    def delete_participant(participant_id: int):
        try:
            return ParticipantService.delete_participant(participant_id=participant_id)
        except AppException as exc:
            raise HTTPException(status_code=exc.code, detail=exc.message) from exc
        except Exception as exc:
            raise HTTPException(status_code=500, detail=str(exc)) from exc
