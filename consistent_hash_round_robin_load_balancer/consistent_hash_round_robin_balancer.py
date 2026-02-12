class RequestInstance:

    def __init__(self, token: str):
        self.token = token

    def __hash__(self):
        return hash(self.token)
    

class Pod:

    def __init__(self, addr: str, port: int) -> None:
        self.port = port
        self.addr = addr

    def __str__(self):
        return f"{self.addr}:{self.port}"
    

class Backend:
    
    def __init__(self, addr: str, port: int, status: bool = False) -> None:
        self.pod = Pod(addr, port)
        self.available = status
    
    def flip_availability(self) -> None:
        self.available = not self.available

    def __hash__(self) -> int:
        return hash(str(self.pod))
        


import bisect


class TrafficBalancer:

    def __init__(self, backends: list) -> None:
        self.backends = dict()
        self.round = list()
        for backend in backends:
            backend_hash = hash(backend)
            bisect.insort(self.round, backend_hash)
            self.backends[backend_hash] = backend
        self.total = len(self.backends)
    
    def add_backend(self, backend: Backend) -> None:
        backend_hash = hash(backend)
        if backend_hash in self.round:
            return
        bisect.insort(self.round, backend_hash)
        self.backends[backend_hash] = backend
        self.total += 1

    def serve_request(self, request: RequestInstance) -> Backend:
        request_hash = hash(request)
        round_idx = bisect.bisect_left(self.round, request_hash % self.total)
        for _ in range(self.total):
            backend_hash = self.round[round_idx % self.total]
            backend: Backend = self.backends[backend_hash]
            if backend.available:
                return backend
            round_idx += 1
        return None


