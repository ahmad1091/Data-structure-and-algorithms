# Sorted Search, No Size: You are given an array-like data structure Listy which lacks a size
# method. It does, however, have an elementAt (i) method that returns the element at index i in
# 0(1) time. If i is beyond the bounds of the data structure, it returns -1. (For this reason, the data
# structure only supports positive integers.) Given a Listy which contains sorted, positive integers,
# find the index at which an element x occurs. If x occurs multiple times, you may return any index.

def binarySearch(arr, x, l, r):

    while l <= r:
        mid = (l + r) // 2
        if x < arr[mid]:
            r = mid - 1
        
        elif x > arr[mid]:
            l = mid + 1

        else:
            return mid

    return -1

def no_size_search(alist, val):
    index = 1
	
    while (elementAt(index) != -1) and (val>alist[index]):
        
        index = index * 2          
            
    
    return binary_search(alist, val, index/2, index)
	
	
print(no_size_search([1,2,3,4,5,9,0,87,45], 87))