class TxnKeyVal:

    def __init__(self) -> None:
        self.transactions = list()
        self.keyval = dict()

    def upsert(self, key: str, val: int) -> None:
        if not self.transactions:
            self.keyval[key] = val
            return
        inner = self.transactions[-1]
        inner[key] = val
    
    def search(self, key: str) -> int:
        if key not in self.keyval:
            return -1
        return self.keyval[key]
    
    def commit(self) -> bool:
        if not self.transactions:
            return False
        inner = self.transactions.pop()
        outer = self.keyval if not self.transactions else self.transactions[-1]
        for key, val in inner.items():
            outer[key] = val
        return True
        
    def transact(self) -> None:
        self.transactions.append(dict())

    def rollback(self) -> bool:
        if not self.transactions: 
            return False
        self.transactions.pop()
        return True
