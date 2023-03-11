
from src.event.infra.repository.protocol import EventRepository

from src.event.domain.entity import Event
from src.event.application.use_case.mapper import dto_to_aggregate




class EventQueryUseCase:
    def __init__(self, event_repository: EventRepository):
        self.event_repository = event_repository

    async def get_all(self) -> list[Event]:
        dtos = await self.event_repository.all_events()
        events = [dto_to_aggregate(dto) for dto in dtos]
        return events
