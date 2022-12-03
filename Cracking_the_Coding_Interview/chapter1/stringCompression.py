# String Compression: Implement a method to perform basic string compression using the counts
# of repeated characters. For example, the string aabcccccaaa would become a2b1c5a3. If the
# "compressed" string would not become smaller than the original string, your method should return
# the original string. You can assume the string has only uppercase and lowercase letters (a - z).

#  BAD solution:
#  The runtime is O(p + k 2), where p is the size of the original string and k is the number of character sequences.
#  It's slow because string concatenation operates in O( n2) time
def compress(s):
    compressedStr = ''
    charCount = 0

    for i in range(len(s)):
        charCount += 1
        if(i+1 >= len(s) or s[i] != s[i+1]):
            compressedStr += (s[i] + str(charCount))
            charCount = 0
    return s if len(compressedStr) > len(s) else compressedStr



# Better solution uses list
def compress(s):
    compressedArr = []
    charCount = 0

    for i in range(len(s)):
        charCount += 1
        if(i+1 >= len(s) or s[i] != s[i+1]):
            compressedArr.append(s[i])
            compressedArr.append(str(charCount))
            charCount = 0

    return s if len(compressedArr) > len(s) else ''.join(compressedArr)

print(compress('aabcccccaaa'))
