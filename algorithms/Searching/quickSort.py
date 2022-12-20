a = [1, 4, 1, 2, 6, 3, 9, 4, 11]

def partition(arr,l,r):
    pivot = arr[r]
    i = l - 1
    for j in range(l, r):
        if arr[j] < pivot:
            i += 1
            arr[i] ,arr[j] = arr[j], arr[i]
    arr[i + 1], arr[r] = arr[r], arr[i + 1]
    return i + 1
        
def quicksort(arr):
    qs(arr, 0, len(arr) - 1)
    
def qs(arr,l,r):
    if l >= r:
        return
    p = partition(arr, l, r)
    
    qs(arr, l, p - 1)
    qs(arr, p+1, r)
    
quicksort(a)

print(a)