# Magic Index: A magic index in an array A [e ... n -1] is defined to be an index such that A[ i] =
# i. Given a sorted array of distinct integers, write a method to find a magic index, if one exists, in
# array A.

# Sol 1:
def magicSlow(arr: list[int]) -> int:
    for i in range(len(arr):
        if arr[i] == i:
            return i
    
    return -1

