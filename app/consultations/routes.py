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


@consultation_router.get("/show-all-consultations", dependencies=[Depends(JWTBearer(["regular_user"]))],
                         response_model=ConsultationSchema)
def read_all_consultations():
    return ConsultationController.read_all_consultations()


@consultation_router.put("/update-consultation", response_model=ConsultationSchema,
                         dependencies=[Depends(JWTBearer(["regular_user"]))])
def update_consultation(request: Request, consultation_id: int, consultation: ConsultationSchemaUpdate):
    updates = consultation.dict(exclude_unset=True, exclude_none=True)
    return ConsultationController.update_consultation(consultation_id=consultation_id, updates=updates, request=request)
