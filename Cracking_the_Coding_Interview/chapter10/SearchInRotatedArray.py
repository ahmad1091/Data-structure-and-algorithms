# Search in Rotated Array: Given a sorted array of n integers that has been rotated an unknown
# number of times, write code to find an element in the array. You may assume that the array was
# originally sorted in increasing order.

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