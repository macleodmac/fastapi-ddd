from dataclasses import dataclass
from uuid import UUID


@dataclass
class Event:
    id: UUID
    # TODO: make these value objects
    key: str
    value: str
