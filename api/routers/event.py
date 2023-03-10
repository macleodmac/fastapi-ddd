from fastapi import APIRouter, Depends
from pydantic import BaseModel

from api.dependencies import list_events_use_case, new_event_use_case
from subdomain.event.use_case.list_events import ListEventCommand, ListEventsUseCase
from subdomain.event.use_case.new_event import NewEventCommand, NewEventUseCase

router = APIRouter(prefix="/events", tags=["events"])


class CreateEventRequest(BaseModel):
    key: str
    value: str


class EventCreatedResponse(BaseModel):
    id: str


@router.post("")
async def create_event(
    request: CreateEventRequest, uc: NewEventUseCase = Depends(new_event_use_case)
) -> EventCreatedResponse:
    event = await uc.invoke(NewEventCommand(key=request.key, value=request.value))
    return EventCreatedResponse(id=str(event.id))


class EventListResponse(BaseModel):
    events: list[EventCreatedResponse]


@router.get("")
async def list_events(
    uc: ListEventsUseCase = Depends(list_events_use_case),
) -> EventListResponse:
    event = await uc.invoke(ListEventCommand())
    return EventListResponse(events=[EventCreatedResponse(id=str(e.id)) for e in event])
