from fastapi import Depends, Request
from src.event.application.use_case.command import EventCommandUseCase
from src.event.application.use_case.query import EventQueryUseCase
from src.event.infra.repository.memory import MemoryEventRepository


async def event_repository(request: Request):
    if hasattr(request.app.state, "event_repository"):
        return request.app.state.event_repository
    else:
        event_repository = MemoryEventRepository()
        request.app.state.event_repository = event_repository
        return event_repository


async def event_command_use_case(
    request: Request,
    event_repository: MemoryEventRepository = Depends(event_repository),
):
    if hasattr(request.app.state, "event_command_use_case"):
        return request.app.state.event_command_use_case
    else:
        use_case = EventCommandUseCase(event_repository)
        request.app.state.event_command_use_case = use_case
        return use_case


async def event_query_use_case(
    request: Request,
    event_repository: MemoryEventRepository = Depends(event_repository),
):
    if hasattr(request.app.state, "event_query_use_case"):
        return request.app.state.event_query_use_case
    else:
        use_case = EventQueryUseCase(event_repository)
        request.app.state.event_query_use_case = use_case
        return use_case
