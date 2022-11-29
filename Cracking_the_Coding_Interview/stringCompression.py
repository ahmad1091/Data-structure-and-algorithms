# String Compression: Implement a method to perform basic string compression using the counts
# of repeated characters. For example, the string aabcccccaaa would become a2b1c5a3. If the
# "compressed" string would not become smaller than the original string, your method should return
# the original string. You can assume the string has only uppercase and lowercase letters (a - z).

#  BAD solution:

def compress(s):
    compressedStr = ''
    charCount = 0

    for i in range(len(s)):
        charCount += 1
        if(i+1 >= len(s) or s[i] != s[i+1]):
            compressedStr += (s[i] + str(charCount))
            charCount = 0
    return s if len(compressedStr) > len(s) else compressedStr


print(compress('aabcccccaaa'))