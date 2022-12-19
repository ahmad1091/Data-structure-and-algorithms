# 846. Hand of Straights

# Alice has some number of cards and she wants to rearrange the cards into groups so that each group is of size groupSize, and consists of groupSize consecutive cards.

# Given an integer array hand where hand[i] is the value written on the ith card and an integer groupSize, return true if she can rearrange the cards, or false otherwise.

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize:
            return False

        countHash = {}
        for n in hand:
            countHash[n] = countHash.get(n, 0) + 1

        minHeap  = list(countHash.keys())
        heapq.heapify(minHeap)

        while minHeap:
            mnVal = minHeap[0]

            for x in range(mnVal, mnVal + groupSize):
                if x not in countHash:
                    return False
                countHash[x] -= 1
                
                if countHash[x] == 0:
                    if x != minHeap[0]:
                        return False
                    heapq.heappop(minHeap)

        return True