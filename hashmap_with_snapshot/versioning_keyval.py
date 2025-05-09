class VersionKeyVal:

    def __init__(self):
        self.keyval, self.histories = {}, {}
        self.snaps = 0

    def search(self, key: str, vers: int = None) -> int:
        if key not in self.keyval or key not in self.histories:
            raise KeyError()
        if vers is None:
            if self.keyval[key] is not None:
                return self.keyval[key]
            raise KeyError()
        if vers > self.snaps:
            raise KeyError()
        # backward traversal for version label
        while 0 <= vers and vers not in self.histories[key]:
            vers -= 1
        # non existence or in deletion before the vers
        if vers < 0 or self.histories[key][vers] is None:
            raise KeyError()
        return self.histories[key][vers]

    def upsert(self, key: str, val: int) -> None:
        self.keyval[key] = val
        if key not in self.histories:
            self.histories[key] = {}
        self.histories[key][self.snaps] = val

    def delete(self, key: str) -> None: 
        if key not in self.keyval or key not in self.histories:
            raise KeyError()
        self.keyval[key] = None
        self.histories[key][self.snaps] = None

    def snapshot(self) -> int:
        vers = self.snaps
        self.snaps += 1
        return vers
