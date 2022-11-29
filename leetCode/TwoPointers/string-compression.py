# 443. String Compression
# Given an array of characters chars, compress it using the following algorithm:

# Begin with an empty string s. For each group of consecutive repeating characters in chars:

# If the group's length is 1, append the character to s.
# Otherwise, append the character followed by the group's length.
# The compressed string s should not be returned separately, but instead, be stored in the input character array chars. Note that group lengths that are 10 or longer will be split into multiple characters in chars.

# After you are done modifying the input array, return the new length of the array.

# You must write an algorithm that uses only constant extra space.


class Solution:
    def compress(self, chars: List[str]) -> int:
        length = len(chars)
        compressedStr = []
        charCount = 0

        for i in range(len(chars)):
            charCount += 1
            
            if(i+1 >= len(chars) or chars[i] != chars[i+1]):
                print(chars[i],charCount)
                compressedStr.append(chars[i])
                if(charCount>1):
                    for x in str(charCount):
                        compressedStr.append(x)
                
                charCount = 0
                
        for x in reversed(compressedStr):
            chars.insert(0,x)  
            
        for i in range(length):
            chars.pop()
              
        print(chars)
        return len(chars)
