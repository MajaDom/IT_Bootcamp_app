from fastapi import APIRouter, Depends
from starlette.requests import Request
from app.participants.controller import ParticipantController
from app.participants.schemas import *
from app.users.controller.user_auth_controller import JWTBearer

participant_router = APIRouter(tags=["Participant"], prefix="/api/participant")


@participant_router.post("/add-new-participant", dependencies=[Depends(JWTBearer(["regular_user"]))],
                         response_model=ParticipantSchema)
def create_new_participant(request: Request, participant: ParticipantSchemaIN, consultation_id: int):
    return ParticipantController.create_new_participant(consultation_id=consultation_id,
                                                        request=request,
                                                        description=participant.description)


@participant_router.get("/show-all-participants", dependencies=[Depends(JWTBearer(["regular_user"]))],
                        response_model=list[ParticipantSchema])
def read_all_participants():
    return ParticipantController.read_all_participants()


@participant_router.get("/show-participants-by-id", dependencies=[Depends(JWTBearer(["regular_user"]))],
                        response_model=list[ParticipantSchema])
def read_participants_of_one_consultation(consultation_id: int):
    return ParticipantController.read_participants_of_one_consultation(consultation_id=consultation_id)


@participant_router.put("/update-participant", response_model=ParticipantSchema,
                        dependencies=[Depends(JWTBearer(["regular_user"]))])
def update_participant(request: Request, participant_id: int, participant: ParticipantSchemaUpdate):
    updates = participant.dict(exclude_unset=True, exclude_none=True)
    return ParticipantController.update_participant(participant_id=participant_id, updates=updates, request=request)


@participant_router.delete("/delete-participant",
                           dependencies=[Depends(JWTBearer(["regular_user"]))])
def delete_participant(participant_id: int):
    return ParticipantController.delete_participant(participant_id=participant_id)
