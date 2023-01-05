# 692. Top K Frequent Words

# Given an array of strings words and an integer k, return the k most frequent strings.

# Return the answer sorted by the frequency from highest to lowest. Sort the words with the same frequency by their lexicographical order.

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        words.sort()
        count = Counter(words)
        sortedItems = sorted(count.items(), key = lambda x: int(x[1]),reverse = True)
        res = []

        for i in range(k):
            res.append(sortedItems[i][0])

        return res