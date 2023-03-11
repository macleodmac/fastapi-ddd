import abc


class AbstractUnitOfWork(abc.ABC):
    def __enter__(self):
        return super().__enter__()

    def __exit__(self, *args):
        return super().__exit__()

    @abc.abstractmethod
    def commit(self):
        raise NotImplementedError

    @abc.abstractmethod
    def rollback(self):
        raise NotImplementedError


class InMemoryUnitOfWork(AbstractUnitOfWork):
    def __enter__(self):
        return super().__enter__()

    def __exit__(self, *args):
        return super().__exit__()

    def commit(self):
        return True

    def rollback(self):
        return True