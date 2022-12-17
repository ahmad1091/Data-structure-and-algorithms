# 1207. Unique Number of Occurrences

# Given an array of integers arr, return true if the number of occurrences of each value in the array is unique or false otherwise.

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        hash = Counter(arr)
        return len(hash.values()) == len(set(hash.values()))