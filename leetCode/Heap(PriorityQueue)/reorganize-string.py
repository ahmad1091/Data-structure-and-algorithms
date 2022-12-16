# 767. Reorganize String

# Given a string s, rearrange the characters of s so that any two adjacent characters are not the same.

# Return any possible rearrangement of s or return "" if not possible.

class Solution:
    def reorganizeString(self, s: str) -> str:
        count = Counter(s)
        maxHeap = [[-cnt, char] for char, cnt in count.items()]
        heapq.heapify(maxHeap)

        prev = None
        res = ''

        while maxHeap or prev:
            if (not maxHeap )and prev:
                return ''

            cnt, char = heapq.heappop(maxHeap)
            cnt += 1
            res += char

            if prev:
                heapq.heappush(maxHeap,prev)
                prev = None

            if cnt != 0:
                prev = [cnt, char]

        return res