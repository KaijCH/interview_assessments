class ValNode:

    def __init__(self, key: str, val: str) -> None:
        self.val = val
        self.key = key
        self.next = None
        self.prev = None


class KeyValO1:

    def __init__(self, maxima: int):
        self.head = ValNode("?", "?")
        self.tail = ValNode("!", "!")
        self.tail.prev = self.head
        self.head.next = self.tail

        self.keyval = {}
        self.maxima = maxima
    
    def search(self, key: str) -> tuple[str, bool]:
        if key not in self.keyval:
            return "", False
        
        vn = self.keyval[key]
        self.__promote(key)
        
        return vn.val, True

    def __promote(self, key: str) -> None:
        vn = self.keyval[key]
        vn.prev.next = vn.next
        vn.next = self.head.next
        vn.prev = self.head
        self.head.next = vn

    def __insert(self, key: str) -> None:
        vn = self.keyval[key]
        if self.tail.prev == self.head:
            self.tail.prev = vn
        vn.next = self.head.next
        vn.prev = self.head
        self.head.next = vn
        

    def __evict(self) -> str:
        vn = self.tail.prev
        vn.prev.next = self.tail
        self.tail.prev = vn.prev
        return vn.key


    def upsert(self, key: str, val: str) -> None:
        vn = ValNode(key, val) if key not in self.keyval else self.keyval[key]
        if key in self.keyval:
            vn.val = val
            self.__promote(key)
            return None
    
        if len(self.keyval) == self.maxima:
            ek = self.__evict()
            self.keyval.pop(ek)

        self.keyval[key] = vn
        self.__insert(key)
        
