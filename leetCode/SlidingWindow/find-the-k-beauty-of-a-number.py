# 2269. Find the K-Beauty of a Number

# The k-beauty of an integer num is defined as the number of substrings of num when it is read as a string that meet the following conditions:

# It has a length of k.
# It is a divisor of num.
# Given integers num and k, return the k-beauty of num.

# Note:

# Leading zeros are allowed.
# 0 is not a divisor of any value.
# A substring is a contiguous sequence of characters in a string.

class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        
        l, r =0, k-1
        numStr = str(num)
        count = 0
        while(r< len(numStr)):
            if((int(numStr[l:r+1])) != 0 and num % (int(numStr[l:r+1])) == 0):
                count+=1
            r += 1
            l += 1
        return count