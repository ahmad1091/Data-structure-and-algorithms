# Peaks and Valleys: In an array of integers, a "peak" is an element which is greater than or equal to
# the adjacent integers and a "valley" is an element which is less than or equal to the adjacent inte-
# gers. For example, in the array {5, 8, 6, 2, 3, 4, 6}, {8, 6} are peaks and {S, 2} are valleys. Given an array
# of integers, sort the array into an alternating sequence of peaks and valleys.

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