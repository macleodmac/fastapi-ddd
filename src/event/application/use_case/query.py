
from src.event.application.unit_of_work import EventUnitOfWork
from src.event.infra.repository.protocol import EventRepository

from src.event.domain.entity import Event
from src.event.application.use_case.mapper import dto_to_aggregate




class EventQueryUseCase:
    def __init__(self, uow: EventUnitOfWork):
        self.uow = uow

    async def get_all(self) -> list[Event]:
        dtos = await self.uow.events.all_events()
        events = [dto_to_aggregate(dto) for dto in dtos]
        return events
