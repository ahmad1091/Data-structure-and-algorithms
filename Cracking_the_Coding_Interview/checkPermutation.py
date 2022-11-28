# Check Permutation: Given two strings, write a method to decide if one is a permutation of the
# other.

# Solution #1: Sort the strings.

def permutation(s,t):
    if len(s) != len(t):
        return False
    return sorted(s) == sorted(t)

print(permutation('abc df','df bca'))

