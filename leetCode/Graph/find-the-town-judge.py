# 997. Find the Town Judge

# In a town, there are n people labeled from 1 to n. There is a rumor that one of these people is secretly the town judge.

# If the town judge exists, then:

# The town judge trusts nobody.
# Everybody (except for the town judge) trusts the town judge.
# There is exactly one person that satisfies properties 1 and 2.
# You are given an array trust where trust[i] = [ai, bi] representing that the person labeled ai trusts the person labeled bi.

# Return the label of the town judge if the town judge exists and can be identified, or return -1 otherwise.

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        N = 1001
        people, trusted = [0] * N, [0] * N
        for p, t in trust:
            people[p] += 1 
            trusted[t] += 1
        for label in range(1, N):
            if people[label] == 0 and trusted[label] == n - 1:
                return label
        return -1