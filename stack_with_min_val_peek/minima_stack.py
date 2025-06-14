class MinimaStack:

    def __init__(self):
        self.elements = []

    def push(self, val: int) -> None:
        minima = val if not self.elements else min(val, self.elements[-1][0])
        curr = (minima, val)
        self.elements.append(curr)
        
    def pop(self) -> None:
        _, val = self.elements.pop()
        return val
        
    def top(self) -> int:
        _, val = self.elements[-1]
        return val
        
    def getMin(self) -> int:
        minima, _ = self.elements[-1]
        return minima
        