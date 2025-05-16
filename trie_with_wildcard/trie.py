import collections

class Trie:

    def __init__(self) -> None:
        self.lookups = {}
        self.halt = "#"
        self.wildcard = "."

    def inserts(self, word: str) -> None:
        layer = self.lookups
        for char in word:
            if char not in layer:
                layer[char] = {}
            layer = layer[char]
        layer[self.halt] = {}

    def explores(self, word: str) -> bool:
        if not word and self.halt not in self.lookups: return False
        layer, idx = self.lookups, 0
        searches = collections.deque([layer])
        while searches and idx < len(word):
            char = word[idx]
            for _ in range(len(searches)):
                layer = searches.popleft()
                
                if char not in layer and char != self.wildcard:
                    continue
                if char != self.wildcard:
                    searches.append(layer[char])
                    break
                for _, sublayer in layer.items():
                    searches.append(sublayer)
            idx += 1
        if not searches:
            return False
        if idx == len(word) and self.halt in searches.popleft():
            return True
        return False
        