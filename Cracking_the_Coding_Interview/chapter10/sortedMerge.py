# Sorted Merge: You are given two sorted arrays, A and B, where A has a large enough buffer at the
# end to hold B. Write a method to merge B into A in sorted order.

def merge(a,b):
    res = []
    
    while a and b:
        if a[0] < b[0]:
            res.append(a.pop(0))
        else:
            res.append(b.pop(0))

    while a:
        res.append(a.pop(0))

    while b:
        res.append(b.pop(0))

    return res

print(merge([4,5,6],[0,1,1,2]))