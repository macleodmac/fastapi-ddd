from fastapi import APIRouter, Depends
from pydantic import BaseModel

from src.event.presentation.dependencies import event_command_use_case, event_query_use_case
from src.event.application.use_case.command import EventCommandUseCase, NewEventCommand
from src.event.application.use_case.query import EventQueryUseCase

router = APIRouter(prefix="/events", tags=["events"])


class CreateEventRequest(BaseModel):
    key: str
    value: str


class EventCreatedResponse(BaseModel):
    id: str


@router.post("")
async def create_event(
    request: CreateEventRequest, uc: EventCommandUseCase = Depends(event_command_use_case)
) -> EventCreatedResponse:
    event = await uc.create_event(NewEventCommand(key=request.key, value=request.value))
    return EventCreatedResponse(id=str(event.id))


class EventListResponse(BaseModel):
    events: list[EventCreatedResponse]


@router.get("")
async def list_events(
    uc: EventQueryUseCase = Depends(event_query_use_case),
) -> EventListResponse:
    events = await uc.get_all()
    return EventListResponse(events=[EventCreatedResponse(id=str(e.id)) for e in events])
