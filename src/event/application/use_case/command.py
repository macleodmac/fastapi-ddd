from uuid import uuid4
from pydantic import BaseModel
from src.event.application.unit_of_work import EventUnitOfWork
from src.event.infra.repository.dto import EventDTO
from src.event.infra.repository.protocol import EventRepository

from src.event.domain.entity import Event
from src.event.application.use_case.mapper import dto_to_aggregate


class NewEventCommand(BaseModel):
    key: str
    value: str


class EventCommandUseCase:
    def __init__(self, uow: EventUnitOfWork):
        self.uow = uow

    async def create_event(self, command: NewEventCommand) -> Event:
        with self.uow as uow:
            dto = await uow.events.insert_event(
                EventDTO(id=uuid4(), key=command.key, value=command.value)
            )
            event = dto_to_aggregate(dto)
            return event
