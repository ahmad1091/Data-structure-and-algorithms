# 1209. Remove All Adjacent Duplicates in String II

# You are given a string s and an integer k, a k duplicate removal consists of choosing k adjacent and equal letters from s and removing them, causing the left and the right side of the deleted substring to concatenate together.

# We repeatedly make k duplicate removals on s until we no longer can.

# Return the final string after all such duplicate removals have been made. It is guaranteed that the answer is unique.


# sol :
class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        charCount = Counter(s)

        for char in charCount:
            if charCount[char]  < k:
                charCount[char] = 0
            else:
                 charCount[char] = charCount[char] - (charCount[char] % k)
    
        res = ''
        for  c in s:
            if charCount[c] > 0:
                charCount[c] -= 1
            else:
                res += c
        
        return res

sol 2:
class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        for c in s:
            if not stack or stack[-1][0] != c:
                stack.append([c, 1])
            else:
                stack[-1][1] += 1
                if stack[-1][1] == k:
                    stack.pop()
        
        res = ''
        for c, count in stack:
            res += c * count
        
        return res
                
                