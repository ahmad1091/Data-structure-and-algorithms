# 239. Sliding Window Maximum

# You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

# Return the max sliding window.

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        l = r = 0
        q = collections.deque()

        while(r < len(nums)):
            while q and nums[q[-1]] < nums[r]:
                q.pop()

            q.append(r)

            if l > q[0]:
                q.popleft()

            if r + 1 >= k:
                res.append(nums[q[0]])
                l += 1

            r += 1

        return res

# sol 2 :
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        q = collections.deque()
        if len(nums) < k:
            k = len(nums)

        for i in range(k):
            while q and nums[q[-1]] <= nums[i]:
                q.pop()
            q.append(i)

        res.append(nums[q[0]])

        for i in range(k, len(nums)):
            while q and nums[q[-1]] <= nums[i]:
                q.pop()
            
            if q and q[0] <= i - k:
                q.popleft()
            
            q.append(i)
            res.append(nums[q[0]])

        return res