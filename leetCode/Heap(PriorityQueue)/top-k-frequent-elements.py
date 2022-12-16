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



