# 819. Most Common Word

# Given a string paragraph and a string array of the banned words banned, return the most frequent word that is not banned.
# It is guaranteed there is at least one word that is not banned, and that the answer is unique.

# The words in paragraph are case-insensitive and the answer should be returned in lowercase.

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        for punc in string.punctuation:
            paragraph = paragraph.replace(punc, " ")

        words = paragraph.lower().split()

        dict = {}
        banned = set(banned)
        for item in words:
            if item not in banned:
                dict[item] = dict.get(item, 0) + 1
                
        return max(dict.keys(), key=(lambda k: dict[k]))