# 557. Reverse Words in a String III

# Given a string s, reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

class Solution:
    def reverseWords(self, s: str) -> str:
        def reverser(string, start, end):
            while start < end:
                string[start], string[end] = string[end], string[start]
                start += 1
                end -= 1
                
        s = re.sub(' +',' ',s.strip())
        s = list(s)
        str_len = len(s)
        reverser(s, 0, str_len - 1)
        wordArr = ''.join(s).split()
        l, r = 0, len(wordArr) - 1
        reverser(wordArr, l, r)
            
        return ' '.join(wordArr)
