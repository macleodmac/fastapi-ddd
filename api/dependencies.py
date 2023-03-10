from fastapi import Depends, Request
from subdomain.event.infrastructure.repository.memory import MemoryEventRepository
from subdomain.event.use_case.list_events import ListEventsUseCase
from subdomain.event.use_case.new_event import NewEventUseCase


async def event_repository(request: Request):
    if hasattr(request.app.state, "event_repository"):
        return request.app.state.event_repository
    else:
        event_repository = MemoryEventRepository()
        request.app.state.event_repository = event_repository
        return event_repository


async def new_event_use_case(
    request: Request,
    event_repository: MemoryEventRepository = Depends(event_repository),
):
    if hasattr(request.app.state, "new_event_use_case"):
        return request.app.state.new_event_use_case
    else:
        use_case = NewEventUseCase(event_repository)
        request.app.state.new_event_use_case = use_case
        return use_case


async def list_events_use_case(
    request: Request,
    event_repository: MemoryEventRepository = Depends(event_repository),
):
    if hasattr(request.app.state, "list_events_use_case"):
        return request.app.state.list_events_use_case
    else:
        use_case = ListEventsUseCase(event_repository)
        request.app.state.list_events_use_case = use_case
        return use_case
