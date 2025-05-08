class VersionKeyVal:
    """
        Implementing a versioning KeyVal class, that supports versioning retrieval from key val storage

    """

    def __init__(self):
        self.keyval, self.persist = {}, {}
        self.snaps = 0

    def search(self, key: str, vers: int = None) -> int:
        if vers is None:
            return self.keyval[key]
        if key not in self.persist:
            raise KeyError()
        if vers > self.snaps:
            raise KeyError()
        while vers >= 0 and vers not in self.persist[key]:
            vers -= 1
        if vers < 0 or self.persist[key][vers] is None:
            raise KeyError()
        return self.persist[key][vers]

    def upsert(self, key: str, val: int) -> None:
        self.keyval[key] = val
        if key not in self.persist:
            self.persist[key] = {}
        self.persist[key][self.snaps] = val

    def delete(self, key: str) -> None:
        self.keyval.pop(key)
        if key not in self.persist:
            self.persist[key] = {}
        self.persist[key][self.snaps] = None

    def snapshot(self) -> int:
        self.snaps += 1
        return self.snaps - 1
