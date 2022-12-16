# 215. Kth Largest Element in an Array

# Given an integer array nums and an integer k, return the kth largest element in the array.

# Note that it is the kth largest element in the sorted order, not the kth distinct element.

# You must solve it in O(n) time complexity.

# sol 1: using built-in sort  O(nlogn)

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort()
        return nums[-k]


# sol 2: using quickSelect O(n)

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        k = len(nums) - k

        def quickSelect(l,r):
            p = l
            for i in range(l,r):
                if nums[r] >= nums[i]:
                    nums[p], nums[i] = nums[i], nums[p]
                    p += 1
            nums[p], nums[r] = nums[r], nums[p]

            if p > k:   return quickSelect(l, p - 1) 
            elif p < k: return quickSelect(p + 1, r) 
            else:       return nums[p]

        return quickSelect(0, len(nums) - 1)

# sol 3: priority queue

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        pq = []
        heapq.heapify(pq)
    
        for i in range(len(nums)):
            heapq.heappush(pq, nums[i])
            if (len(pq) > k):
                heapq.heappop(pq)

        return pq[0]