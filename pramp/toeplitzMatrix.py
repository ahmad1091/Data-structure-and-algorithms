Toeplitz Matrix
A Toeplitz matrix is a matrix where every left-to-right-descending diagonal has the same element. Given a non-empty matrix arr, write a function that returns true if and only if it is a Toeplitz matrix. The matrix can be any dimensions, not necessarily square.

def isToeplitz(arr):
  pattern = {}
  for r in range(len(arr)):
    for c in range(len(arr[0])):
      if r - c in pattern:
        if pattern[r - c] != arr[r][c]: return False
      else:
        pattern[r - c] = arr[r][c]
        
  return True

