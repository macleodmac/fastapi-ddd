from typing import Protocol
from uuid import UUID

from subdomain.event.infrastructure.dto import EventDTO


class MemoryEventRepository:
    def __init__(self) -> None:
        self._events: dict[UUID, EventDTO] = {}

    async def insert_event(self, event: EventDTO) -> EventDTO:
        self._events[event.id] = event
        return event

    async def all_events(self) -> list[EventDTO]:
        return list(self._events.values())
