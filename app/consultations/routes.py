from fastapi import APIRouter, Depends
from starlette.requests import Request
from app.consultations.controller import ConsultationController
from app.consultations.schemas import *
from app.users.controller.user_auth_controller import JWTBearer

consultation_router = APIRouter(tags=["consultation"], prefix="/api/consultation")


@consultation_router.post("/add-new-consultation", dependencies=[Depends(JWTBearer(["regular_user"]))],
                          response_model=ConsultationSchema)
def create_new_consultation(request: Request, consultation: ConsultationSchemaIN):
    return ConsultationController.create_new_consultation(topic=consultation.topic,
                                                          description=consultation.description,
                                                          request=request)
