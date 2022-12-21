# Sorted Merge: You are given two sorted arrays, A and B, where A has a large enough buffer at the
# end to hold B. Write a method to merge B into A in sorted order.

# sol 1 :
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

# sol 2: without allocate additional space
def merge(a,b):
    aIdx = len(a) - 1
    bIdx = len(b) - 1
    mergeIdx = len(a) + len(b) - 1

    while bIdx >= 0:
        if aIdx >= 0 and a[aIdx] > b[bIdx]:
            a[mergeIdx] = a[aIdx]
            aIdx -= 1
        else:
            a[mergeIdx] = b[bIdx]
            bIdx -= 1

        mergeIdx -= 1

a = [2,2,4,5,6]
b = [0,1,1,2]

merge(a,b)
print(a)

