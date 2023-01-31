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

# sol 2: optimal 
class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        res = []
        min_pq = []
        max_pq = []

        def getMedian():
            if not min_pq and not max_pq: return 0
            if len(min_pq) != len(max_pq):
                return min_pq[0]
            else:
                return (min_pq[0] - max_pq[0]) / 2

        def balancePQ():
            if len(max_pq) > len(min_pq):
                heapq.heappush(min_pq, -heapq.heappop(max_pq))
            if len(min_pq) - len(max_pq) > 1:
                heapq.heappush(max_pq, -heapq.heappop(min_pq))

        def insert(num):
            median = getMedian()

            if num >= median:
                heapq.heappush(min_pq, num)
            else:
                heapq.heappush(max_pq, -num)

            balancePQ()

        def remove(num):
            median = getMedian()

            if num >= median:
                min_pq.remove(num)
                heapq.heapify(min_pq)
            else:
                max_pq.remove(-num)
                heapq.heapify(max_pq)

            balancePQ()

        for i in range(len(nums)):
            insert(nums[i])

            if i >= k:
                remove(nums[i - k])
            if i >= k - 1:
                res.append(getMedian())

        return res

            