class OrderedStream:

    def __init__(self, n: int):
        self.pairs = dict()
        self.pointer = 0

    def insert(self, idKey: int, value: str) -> list[str]:
        self.pairs[idKey] = value

        temp = list()
        while self.pointer + 1 in self.pairs:
            self.pointer += 1

            temp.append(self.pairs[self.pointer])

        return temp