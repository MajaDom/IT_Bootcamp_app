from fastapi import APIRouter
from app.consultations.controller import ConsultationController
from app.consultations.schemas import *

consultation_router = APIRouter(tags=["consultation"], prefix="/api/consultation")


@consultation_router.post("/add-new-consultation", response_model= ConsultationSchema)
def create_new_consultation(consultation: ConsultationSchemaIN):
    return ConsultationController.create_new_consultation(topic=consultation.topic,
                                                          description=consultation.description,
                                                          user_id=consultation.user_id)
