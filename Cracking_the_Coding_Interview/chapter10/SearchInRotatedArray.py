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