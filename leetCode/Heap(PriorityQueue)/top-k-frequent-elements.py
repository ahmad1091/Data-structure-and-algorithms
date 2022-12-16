347. Top K Frequent Elements

Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

# solution 1: using Hash
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict = {}
        for item in nums:
            dict[item] = dict.get(item, 0) + 1
        a = sorted(dict.keys(), key=(lambda k: dict[k]))
        
        return a[-k:]


# solution 1: using max_heap

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = collections.Counter(nums)
        max_heap = []
        print(counts)
        for key, val in counts.items():
            heapq.heappush(max_heap, (-val, key))
        
        result = []
        while k > 0:
            result.append(heapq.heappop(max_heap)[1])
            k -= 1
        
        return result