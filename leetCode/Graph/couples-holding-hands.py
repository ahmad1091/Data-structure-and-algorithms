# 765. Couples Holding Hands

# There are n couples sitting in 2n seats arranged in a row and want to hold hands.

# The people and seats are represented by an integer array row where row[i] is the ID of the person sitting in the ith seat. The couples are numbered in order, the first couple being (0, 1), the second couple being (2, 3), and so on with the last couple being (2n - 2, 2n - 1).

# Return the minimum number of swaps so that every couple is sitting side by side. A swap consists of choosing any two people, then they stand up and switch seats.

class Solution:
    def minSwapsCouples(self, row: List[int]) -> int:
        # this hash to store the current index for each couple
        coupleToIndex = {c:i for i, c in enumerate(row)}
        swaps = 0

        # move tow steps for couples 
        for i in range(0, len(row), 2):
            a, b = row[i], row[i + 1]
            if a // 2 == b // 2: continue # means a & b is a couple

            # find actual couple for the current one
            # if the couple is odd then its pair would be the prev number otherwise it would be the next number
            couple = a - 1 if a % 2 else a + 1

            # get the index for the couple pair 
            coupleIndex = coupleToIndex[couple]

            #swap the current neighbor with the actual couple
            row[i + 1], row[coupleIndex] = row[coupleIndex], row[i + 1]

            # update the indices for the swapped couples
            coupleToIndex[couple] = i + 1
            coupleToIndex[b] = coupleIndex
            swaps += 1

        return swaps