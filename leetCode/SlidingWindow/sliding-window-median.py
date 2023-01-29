# 480. Sliding Window Median

# The median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value. So the median is the mean of the two middle values.

# For examples, if arr = [2,3,4], the median is 3.
# For examples, if arr = [1,2,3,4], the median is (2 + 3) / 2 = 2.5.
# You are given an integer array nums and an integer k. There is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

# Return the median array for each window in the original array. Answers within 10-5 of the actual value will be accepted.

class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        n = len(nums)
        cur = nums[:k - 1]
        ans = [] 

        for i in range(k - 1, n):
            if i > k - 1:
                cur.pop(0)
            cur.append(nums[i])

            sortedArr = sorted(cur)

            if k % 2:
                ans.append(sortedArr[k // 2])
            else:
                ans.append((sortedArr[k // 2] + sortedArr[k // 2 - 1]) / 2)

        return ans