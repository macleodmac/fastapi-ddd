from fastapi import Depends, Request
from src.event.application.unit_of_work import EventUnitOfWork
from src.event.application.use_case.command import EventCommandUseCase
from src.event.application.use_case.query import EventQueryUseCase
from src.event.infra.repository.memory import MemoryEventRepository


async def in_memory_store(request: Request):
    if hasattr(request.app.state, "in_memory_store"):
        return request.app.state.in_memory_store
    else:
        in_memory_store = {}
        request.app.state.in_memory_store = in_memory_store
        return in_memory_store


async def event_unit_of_work(request: Request, in_memory_store: dict = Depends(in_memory_store)):
    if hasattr(request.app.state, "event_unit_of_work"):
        return request.app.state.event_unit_of_work
    else:
        event_unit_of_work = EventUnitOfWork(in_memory_store)
        request.app.state.event_unit_of_work = event_unit_of_work
        return event_unit_of_work



async def event_command_use_case(
    request: Request,
    event_uow: EventUnitOfWork = Depends(event_unit_of_work),
):
    if hasattr(request.app.state, "event_command_use_case"):
        return request.app.state.event_command_use_case
    else:
        use_case = EventCommandUseCase(event_uow)
        request.app.state.event_command_use_case = use_case
        return use_case


async def event_query_use_case(
    request: Request,
    event_uow: EventUnitOfWork = Depends(event_unit_of_work),
):
    if hasattr(request.app.state, "event_query_use_case"):
        return request.app.state.event_query_use_case
    else:
        use_case = EventQueryUseCase(event_uow)
        request.app.state.event_query_use_case = use_case
        return use_case
