# 217. Contains Duplicate

# Share
# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hash = {}
                
        for i in range(len(nums)):
            hash[nums[i]] = "null"
        
        for i in range(len(nums)):
            if(hash[nums[i]] != "null"):
                return True
            hash[nums[i]] = i 
        
        return False
        