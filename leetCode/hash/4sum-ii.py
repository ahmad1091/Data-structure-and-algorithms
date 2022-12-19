# 454. 4Sum II

# Given four integer arrays nums1, nums2, nums3, and nums4 all of length n, return the number of tuples (i, j, k, l) such that:

# 0 <= i, j, k, l < n
# nums1[i] + nums2[j] + nums3[k] + nums4[l] == 0

class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        counter = defaultdict(int)

        for w in nums1:
            for x in nums2:
                counter[w + x] += 1

        res = 0
        for y in nums3:
            for z in nums4:
                res += counter[-(y + z)]

        return res