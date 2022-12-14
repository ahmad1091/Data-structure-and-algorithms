# Sort Stack: Write a program to sort a stack such that the smallest items are on the top. You can use
# an additional temporary stack, but you may not copy the elements into any other data structure
# (such as an array) . The stack supports the following operations: push, pop, peek, and isEmpty.

def sort(s):
    r = []

    while(s):
        temp = s.pop()
        while r and temp < r[-1]:
            s.append(r.pop())

        r.append(temp)

    while r:
        s.append(r.pop())
