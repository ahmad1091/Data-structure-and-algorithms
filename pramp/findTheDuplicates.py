Find The Duplicates
Given two sorted arrays arr1 and arr2 of passport numbers, implement a function findDuplicates that returns an array of all passport numbers that are both in arr1 and arr2. Note that the output array should be sorted in an ascending order.

Let N and M be the lengths of arr1 and arr2, respectively. Solve for two cases and analyze the time & space complexities of your solutions: M ≈ N - the array lengths are approximately the same M ≫ N - arr2 is much bigger than arr1.

def find_duplicates(arr1, arr2):
  a, b = 0, 0
  res = []
  
  while a < len(arr1) and b < len(arr2):
    if arr1[a] == arr2[b]:
      res.append(arr1[a])
      a += 1
      b += 1
    elif arr1[a] < arr2[b]:
      a += 1
    else:
      b += 1
      
  return res