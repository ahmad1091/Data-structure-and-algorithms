# 1588. Sum of All Odd Length Subarrays

# Given an array of positive integers arr, return the sum of all possible odd-length subarrays of arr.

# A subarray is a contiguous subsequence of the array.

class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        
        sumArr = [0] * len(arr)
        sumArr[0] = arr[0]
        oddLengths = []
        for i in range(1,len(arr)+1):
            if i % 2 != 0:
                oddLengths.append(i)
                
        for i in range(1,len(arr)):
            sumArr[i] = sumArr[i-1] + arr[i]
        
        total = 0
        for n in oddLengths:
            i = 0
            while(n+i-1 < len(sumArr)):
                if i - 1 < 0:
                    total += sumArr[n+i-1] 
                else:
                    total += (sumArr[n+i-1] - sumArr[i-1])
                i += 1
        return total
