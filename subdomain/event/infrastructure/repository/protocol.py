from typing import Protocol

from subdomain.event.infrastructure.dto import EventDTO


class EventRepository(Protocol):
    async def insert_event(self, event: EventDTO) -> EventDTO:
        ...

    async def all_events(self) -> list[EventDTO]:
        ...
