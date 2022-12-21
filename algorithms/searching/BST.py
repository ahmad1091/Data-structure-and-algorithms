
# sol 1: using loop
def binarySearch(arr, x):
    l = arr[0]
    r = len(arr) - 1

    while l <= r:
        mid = (l + r) / 2
        if x < arr[mid]:
            r = mid - 1
        
        elif x > arr[mid]:
            l = mid + 1

        else:
            return mid

    return -1

# sol 1: using recursion
def binarySearch(arr, x, l, r):
    if l > r: return -1

    mid = (r + l) / 2
    if x < arr[mid]:
        return binarySearch(arr[:mid - 1], x, l, mid - 1)

        
    elif x > arr[mid]:
        return binarySearch(arr[mid + 1:], x, mid + 1, r)

    else:
        return mid



