from uuid import uuid4
from pydantic import BaseModel
from subdomain.event.infrastructure.dto import EventDTO
from subdomain.event.infrastructure.repository.protocol import EventRepository

from subdomain.event.model import Event
from subdomain.event.use_case.mapper import dto_to_aggregate


class ListEventCommand(BaseModel):
    ...


class ListEventsUseCase:
    def __init__(self, event_repository: EventRepository):
        self.event_repository = event_repository

    async def invoke(self, command: ListEventCommand) -> list[Event]:
        dtos = await self.event_repository.all_events()
        events = [dto_to_aggregate(dto) for dto in dtos]
        return events
