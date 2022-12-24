# 4. Median of Two Sorted Arrays

# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

# The overall run time complexity should be O(log (m+n)).

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        s = sorted(nums1 + nums2)
        m = len(s) // 2
        if len(s) % 2:
            return s[m]
        else:
            return (s[m-1] + s[m]) / 2