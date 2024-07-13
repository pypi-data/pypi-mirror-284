class BucketNotFoundError(KeyError):
    pass


class DocumentNotFoundError(KeyError):
    pass


class ChunkNotFoundError(KeyError):
    pass


class CommitFailedError(RuntimeError):
    pass


class InvalidPrefixError(KeyError):
    pass


class CommitNotFoundException(KeyError):
    pass


class SessionNotFoundException(KeyError):
    pass
