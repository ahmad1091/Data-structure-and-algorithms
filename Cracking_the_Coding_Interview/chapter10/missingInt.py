# Missing Int: Given an input file with four billion non-negative integers, provide an algorithm to
# generate an integer that is not contained in the file. Assume you have 1 GB of memory available for
# this task.

# There are a total of 2 32 , or 4 billion, distinct integers possible and 2 31 non-negative integers. Therefore, we
# know the input file (assuming it is ints rather than longs) contains some duplicates.
# We have 1 GB of memory, or 8 billion bits. Thus, with 8 billion bits, we can map all possible integers to a
# d istinct bit with the available memory. The logic is as follows:
# 1. Create a bit vector (BV) with 4 billion bits. Recall that a bit vector is an array that compactly stores
# boolean va lues by using an array of ints (or another data type). Each int represents 32 boolean values.
# 2. Initialize BV with all Os.
# 3. Scan all numbers (nurn) from the file and call BV. set (nurn, 1).
# 4. Now scan again BV from the Oth index.
# 5. Return the first index which has a value of 0.