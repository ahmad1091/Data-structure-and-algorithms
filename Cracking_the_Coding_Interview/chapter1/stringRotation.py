# String Rotation: Assume you have a method i5Substring which checks if one word is a substring
# of another. Given two strings, 51 and 52, write code to check if 52 is a rotation of 51 using only one
# call to isSubstring (e.g., "waterbottleuis" a rotation of "uerbottlewat").

# Solution 1 :

class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        first = goal[0]
        
        for i in range(len(s)):
            if(s[i] == first):
                if(s[i:] == goal[:len(s[i:])] and s[:i] == goal[len(s[i:]):]):
                    return True
            
        return False    

# Solution 2 :

def isRotation(s1,s2):
    length = len(s1)
    if length == len(s2) and length > 0:
        return s2 in s1*2
    return False

print(isRotation('waterbottle','erbottlewat'))



