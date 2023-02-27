# 727. Minimum Window Subsequence

# Given strings s1 and s2, return the minimum contiguous substring part of s1, so that s2 is a subsequence of the part.

# If there is no such window in s1 that covers all characters in s2, return the empty string "". If there are multiple such minimum-length windows, return the one with the left-most starting index.

## algorithm 
# Initialize two pointers index_s1 and index_s2 to 0 to iterate both the strings.

# If the character pointed by index_s1 in s1 is the same as the character pointed by index_s2 in s2, increment both pointers.

# Create two new pointers (start and end) once index_s2 reaches the end of s2.

# Set the start to the value of index_s1 and end to start + 1.

# Decrement the start pointer until index_s2 becomes less than 0.

# Decrement index_s2 only if the character pointed by the start pointer in s1 is equal to the character pointed to by index_s2 in s2.

# Calculate the length of a substring by subtracting values of the end and start variables.

# If this length is less than the current minimum length, update the length variable and min_subsequence string.

# Repeat until index_s1 reaches the end of s1.

def min_window(s1, s2):
    size1, size2 = len(s1), len(s2)
    length = float('inf')
    idx_s1 = idx_s2 = 0
    minSub = ''

    while idx_s1 < size1:
        if s1[idx_s1] == s2[idx_s2]:
            idx_s2 += 1
            if idx_s2 == size2:
                start, end = idx_s1, idx_s1 + 1
                idx_s2 -= 1
                while idx_s2 >= 0:
                    if s1[start] == s2[idx_s2]:
                        idx_s2 -= 1
                    start -= 1
                start += 1
                if end - start  < length:
                    length = end - start
                    minSub = s1[start:end]
        idx_s1 += 1
    
    return minSub