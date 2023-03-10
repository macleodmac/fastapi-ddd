from uuid import uuid4
from pydantic import BaseModel
from subdomain.event.infrastructure.dto import EventDTO
from subdomain.event.infrastructure.repository.protocol import EventRepository

from subdomain.event.model import Event
from subdomain.event.use_case.mapper import dto_to_aggregate


class NewEventCommand(BaseModel):
    key: str
    value: str


class NewEventUseCase:
    def __init__(self, event_repository: EventRepository):
        self.event_repository = event_repository

    async def invoke(self, command: NewEventCommand) -> Event:
        dto = await self.event_repository.insert_event(
            EventDTO(id=uuid4(), key=command.key, value=command.value)
        )
        event = dto_to_aggregate(dto)
        return event
