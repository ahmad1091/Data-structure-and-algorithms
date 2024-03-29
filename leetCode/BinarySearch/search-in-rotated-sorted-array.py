# 33. Search in Rotated Sorted Array

# There is an integer array nums sorted in ascending order (with distinct values).

# Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

# Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

# You must write an algorithm with O(log n) runtime complexity.

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        direction = 0 if nums[0] < target else len(nums) - 1
        if direction:
            for i in range(len(nums)-1, -1, -1):
                if nums[i] == target:
                    return i
        else:
            for i in range(len(nums)):
                if nums[i] == target:
                    return i
        return -1


# sol 2:

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2
            if target == nums[mid]:
                return mid

            if nums[l] <= nums[mid]:
                if target > nums[mid] or target < nums[l]:
                    l = mid + 1
                else:
                    r = mid - 1

            else:
                if target < nums[mid] or target > nums[r]:
                    r = mid - 1
                else:
                    l = mid + 1

        return -1 

# sol 3:
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return self.binary_search(nums, 0, len(nums) - 1, target)

    def binary_search(self, nums: List[int], low: int, high:int, target: int):
        if low > high: return -1

        mid = (high + low) >> 1

        if nums[mid] == target: return mid

        if nums[low] <= nums[mid]:
            if nums[low] <= target < nums[mid]:
                return self.binary_search(nums, low, mid - 1, target)
            else:
                return self.binary_search(nums, mid + 1, high, target)
        else:
            if nums[mid] < target <= nums[high]:
                return self.binary_search(nums, mid + 1, high, target)
            else:
                return self.binary_search(nums, low, mid - 1, target)