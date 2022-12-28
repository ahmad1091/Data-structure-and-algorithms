# Magic Index: A magic index in an array A [e ... n -1] is defined to be an index such that A[ i] =
# i. Given a sorted array of distinct integers, write a method to find a magic index, if one exists, in
# array A.

# Sol 1:
def magicSlow(arr: list[int]) -> int:
    for i in range(len(arr):
        if arr[i] == i:
            return i
    
    return -1

# Sol 2: BST
def magicFast(array: list[int]) -> int:
    def magicFast(array: list[int], start: int, end: int) -> int:
        if end < start: return -1
        mid = (start + end) // 2
        if (array[mid] == mid):
            return mid
        elif (array[mid] > mid):
            return magicFast(array, start, mid - 1)
        else:
            ret urn magicFast(array, mid + 1, end)

    return magicFast(array)
