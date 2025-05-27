import collections

class Trie:

    def __init__(self) -> None:
        self.lookups = {}
        self.halt = "#"
        self.wildcard = "."
        self.occurs = "*"

    def inserts(self, word: str) -> None:
        layer = self.lookups
        for char in word:
            if char not in layer:
                layer[char] = {}
            layer = layer[char]
        layer[self.halt] = {}

    def explores(self, word: str) -> bool:
        if not word and self.halt not in self.lookups: 
            return False
        length, layer, seen = len(word), self.lookups, set()
        # (layer of trie, idx of word match)
        searches = collections.deque([(layer, 0)])
        while searches:
            layer, idx = searches.popleft()
            memo = (id(layer), idx)
            if memo in seen: 
                continue
            seen.add(memo)
            # complete match with trie <> word
            if idx == length and self.halt in layer:
                return True
            # use up curr path, ignore
            if idx == length:
                continue
            char = word[idx]
            # unmatch char in trie, ignore
            if char not in layer and char != self.wildcard:
                continue
            # match char with layer, further search
            if char != self.wildcard:
                searches.append((layer[char], idx + 1))
                continue
            # single wildcard match, continue all possible sublayer trie
            if idx == length - 1 or idx + 1 < length and word[idx + 1] != self.occurs:
                for sublayer in layer.values():
                    searches.append( (sublayer, idx + 1) )
                continue
            # multiple wildcard match, if wildcard consume none char in word
            searches.append((layer, idx + 2))
            # multiple wildcard match, if wildcard consume more char in word, using dfs for route consistence
            for key, sublayer in layer.items():
                while key in sublayer:
                    searches.append((sublayer, idx + 2))
                    sublayer = sublayer[key]
                searches.append((sublayer, idx + 2))
        return False
                