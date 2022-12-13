# 682. Baseball Game

# You are keeping the scores for a baseball game with strange rules. At the beginning of the game, you start with an empty record.

# You are given a list of strings operations, where operations[i] is the ith operation you must apply to the record and is one of the following:

# An integer x.
# Record a new score of x.
# '+'.
# Record a new score that is the sum of the previous two scores.
# 'D'.
# Record a new score that is the double of the previous score.
# 'C'.
# Invalidate the previous score, removing it from the record.
# Return the sum of all the scores on the record after applying all the operations.

# The test cases are generated such that the answer and all intermediate calculations fit in a 32-bit integer and that all operations are valid.

#  sol1:
class Solution:
    def operate(self, op: str, arr: List[int]) -> List[int]:
        match op:
            case '+':
                arr.append(arr[-1] + arr[-2])
            case 'D':
                arr.append(2 * arr[-1])
            case 'C':
                arr.pop()
            case _:
                arr.append(int(op))

    def calPoints(self, operations: List[str]) -> int:
        arr =[]
        for x in operations:
            self.operate(x,arr)
    
        return sum(arr)
# sol 2: more optimal
class Solution:
    def operate(self, op: str, arr: List[int]) -> List[int]:
        match op:
            case '+':
                return arr[-1] + arr[-2]
            case 'D':
                return 2 * arr[-1]
            case 'C':
                return arr.pop() and None
            case _:
                return int(op)

    def calPoints(self, operations: List[str]) -> int:
        arr =[]
        for x in operations:
            val = self.operate(x,arr)
            if val:
                arr.append(val)
    
        return sum(arr)
