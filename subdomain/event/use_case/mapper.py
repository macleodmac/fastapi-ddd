from subdomain.event.infrastructure.dto import EventDTO
from subdomain.event.model import Event


def dto_to_aggregate(dto: EventDTO) -> Event:
    return Event(id=dto.id, key=dto.key, value=dto.value)
