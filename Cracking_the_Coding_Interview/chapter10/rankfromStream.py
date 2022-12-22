# Rank from Stream: Imagine you are reading in a stream of integers. Periodically, you wish to be able
# to look up the rank of a number x (the number of values less than or equal to x). Implement the data
# structures and algorithms to support these operations. That is, implement the method track (int
# x) , w hich is called when each number is generated, and the method getRankOfNumber(int
# x) , which returns the number of values less than or equal to X (not including x itself).

class BinaryIndexedTree:
    def __init__(self, n):
        self.n = n
        self.c = [0] * (n + 1)

    @staticmethod
    def lowbit(x):
        return x & -x

    def update(self, x, delta):
        while x <= self.n:
            self.c[x] += delta
            x += BinaryIndexedTree.lowbit(x)

    def query(self, x):
        s = 0
        while x > 0:
            s += self.c[x]
            x -= BinaryIndexedTree.lowbit(x)
        return s


class StreamRank:
    def __init__(self):
        self.tree = BinaryIndexedTree(50010)

    def track(self, x: int) -> None:
        self.tree.update(x + 1, 1)

    def getRankOfNumber(self, x: int) -> int:
        return self.tree.query(x + 1)


# Your StreamRank object will be instantiated and called as such:
# obj = StreamRank()
# obj.track(x)
# param_2 = obj.getRankOfNumber(x)