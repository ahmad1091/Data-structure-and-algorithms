# 219. Contains Duplicate II

# Share
# Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.

# Solution 1:
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hash = {}
                
        for i in range(len(nums)):
            hash[nums[i]] = "null"
        
        for i in range(len(nums)):
            if((hash[nums[i]] != "null")and abs(hash[nums[i]]-i) <= k):
                return True
            hash[nums[i]] = i 
        
        return False

# Solution 2:
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        index_map = {}

        for i in range(len(nums)):
            num = nums[i]
            if num in index_map and i - index_map[num] <= k:
                return True
            index_map[num] = i

        return False
            
        
            