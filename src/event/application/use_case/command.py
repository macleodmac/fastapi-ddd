from uuid import uuid4
from pydantic import BaseModel
from src.event.infra.repository.dto import EventDTO
from src.event.infra.repository.protocol import EventRepository

from src.event.domain.entity import Event
from src.event.application.use_case.mapper import dto_to_aggregate


class NewEventCommand(BaseModel):
    key: str
    value: str


class EventCommandUseCase:
    def __init__(self, event_repository: EventRepository):
        self.event_repository = event_repository

    async def create_event(self, command: NewEventCommand) -> Event:
        dto = await self.event_repository.insert_event(
            EventDTO(id=uuid4(), key=command.key, value=command.value)
        )
        event = dto_to_aggregate(dto)
        return event
