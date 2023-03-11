from src.event.infra.repository.dto import EventDTO
from src.event.domain.entity import Event


def dto_to_aggregate(dto: EventDTO) -> Event:
    return Event(id=dto.id, key=dto.key, value=dto.value)
