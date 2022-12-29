# Recursive Multiply: Write a recursive function to multiply two positive integers without using the
# * operator. You can use addition, subtraction, and bit shifting, but you should minimize the number
# of those operations.

def multiply(A: int, B: inr) -> int {
    if A == 0 or B == 0:
        return 0

    max, min = max(A, B), min(A, B)
    return max + multiply(max, min - 1);
