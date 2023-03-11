


from src.event.infra.repository.memory import MemoryEventRepository




# TODO: use a mixin for common functionality

class EventUnitOfWork:

    events: MemoryEventRepository

    def __init__(self, storage: dict):
        self.storage = storage
    
    def __enter__(self):
        self.events = MemoryEventRepository(self.storage)
        return self

    def __exit__(self, *args):
        ...

    def commit(self):
        ...

    def rollback(self):
        ...