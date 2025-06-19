class Compressor:

    def __init__(self):
        self.records = list()
        self.last = ""

    def reset(self) -> None:
        self.records = list()
        self.last = ""

    def __generate(self) -> str:
        repres = list()
        for item in self.records:
            repres.append(item.output())
        return  "".join(repres)
    
    def compress(self, strin: str) -> str:
        read, length  = 0, len(strin)
        while self.last and read < length and strin[read] == self.last :
            read += 1
        if self.records and read != 0:
            self.records[-1].increase(read)
        
        current = list()
        while read < length:
            symbol = strin[read]
            mark = read + 1
            while mark < length and strin[mark] == symbol:
                mark += 1
            curr = Compo(strin[read], mark - read)
            current.append(curr)
            read = mark
        
        self.records += current
        if strin:
            self.last = strin[-1]
        
        return self.__generate()


class Compo:

    def __init__(self, symbol: str, count: int) -> None:
        self.symbol = symbol
        self.count = count
        self.repre = symbol if not symbol.isdigit() else "_" + symbol
    
    def increase(self, more: int) -> None:
        self.count += more

    def output(self) -> str:
        return self.repre + (str(self.count) if self.count > 1 else "")

    def __repr__(self) -> str:
        return str(self.symbol) + ":" + str(self.count)
