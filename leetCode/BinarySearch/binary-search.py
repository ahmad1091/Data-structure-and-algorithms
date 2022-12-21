# 704. Binary Search

# Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

# You must write an algorithm with O(log n) runtime complexity.

# sol 1: recursion
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def BS(arr, x, l, r):
            if l > r: return -1
            
            mid = (l + r) // 2

            if target < nums[mid]:
                return BS(arr, x, l, mid - 1)
            elif target > nums[mid]:
                return BS(arr, x, mid+1, r)
            else:
                return mid

        return BS(nums, target, 0, len(nums) - 1)

# sol 2: loop
