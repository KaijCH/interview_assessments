import collections


class DynamicConnect:

    def __init__(self, nodes: int) -> None:
        self.alives = [False for _ in range(nodes)]
        self.conns = collections.defaultdict(set)
        self.components = 0
        
    def activates(self, node: int) -> None:
        self.alives[node] = True
        self.components += 1

    def deactivates(self, node: int) -> None:
        for neigh in list(self.conns[node]):
            self.disconnects(node, neigh)
        self.alives[node] = False
        self.components -= 1
        
    def connects(self, fst: int, snd: int) -> None:
        if not self.alives[fst] or not self.alives[snd] or snd in self.conns[fst]:
            return
        if not self.connected(fst, snd):
            self.components -= 1
        self.conns[fst].add(snd)
        self.conns[snd].add(fst)
    
    def disconnects(self, fst: int, snd: int) -> None:
        if snd in self.conns[fst]:
            self.conns[fst].remove(snd)
            self.conns[snd].remove(fst)
            if not self.connected(snd, fst):
                self.components += 1

    def connected(self, fst: int, snd: int) -> bool:
        if not self.alives[fst] or not self.alives[snd]:
            return False
        queue = collections.deque([fst])
        seen = set()
        while queue:
            last = queue.popleft()
            seen.add(last)
            if snd in self.conns[last]: 
                return True
            for this in self.conns[last]:
                if this in seen: 
                    continue
                queue.append(this)
        return False

    def counts(self) -> int:
        return self.components