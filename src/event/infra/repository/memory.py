from typing import Protocol
from uuid import UUID

from src.event.infra.repository.dto import EventDTO

    


class MemoryEventRepository:
    def __init__(self, storage: dict) -> None:
        self._storage = storage

    async def insert_event(self, event: EventDTO) -> EventDTO:
        self._storage[event.id] = event
        return event

    async def all_events(self) -> list[EventDTO]:
        return list(self._storage.values())
