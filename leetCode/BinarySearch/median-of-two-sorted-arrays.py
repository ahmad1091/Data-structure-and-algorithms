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


# sol 2: BS solution 
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        a, b = nums1, nums2
        total = len(a) + len(b)
        half = total // 2
        
        if len(a) > len(b):
            a, b = b, a

        l, r = 0, len(a) - 1
        while True:
            i = (r + l) // 2
            j = half - i - 2

            aleft = a[i] if i >= 0 else float('-inf')
            aright = a[i + 1] if i + 1 < len(a) else float('inf')
            bleft = b[j] if j >= 0 else float('-inf')
            bright = b[j + 1] if j + 1 < len(b) else float('inf')

            if aleft <= bright and bleft <= aright:
                if total % 2:
                    return min(aright,bright)
                return (max(aleft,bleft) + min(aright,bright)) /2 
            elif aleft > bright:
                r = i - 1
            else:
                l = l + 1         