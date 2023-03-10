from dataclasses import dataclass
from uuid import UUID


@dataclass
class EventDTO:
    id: UUID
    key: str
    value: str
