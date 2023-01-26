# 721. Accounts Merge

# Given a list of accounts where each element accounts[i] is a list of strings, where the first element accounts[i][0] is a name, and the rest of the elements are emails representing emails of the account.

# Now, we would like to merge these accounts. Two accounts definitely belong to the same person if there is some common email to both accounts. Note that even if two accounts have the same name, they may belong to different people as people could have the same name. A person can have any number of accounts initially, but all of their accounts definitely have the same name.

# After merging the accounts, return the accounts in the following format: the first element of each account is the name, and the rest of the elements are emails in sorted order. The accounts themselves can be returned in any order.

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        graph = defaultdict(set)
        toName = {}

        for account in accounts:
            name = account[0]
            for email in account[1:]:
                graph[email].add(account[1])
                graph[account[1]].add(email)
                toName[email] = name

        visit = set()
        res = []

        for email in graph:
            if email not in visit:
                visit.add(email)
                stack = [email]
                temp = []
                while stack:
                    node = stack.pop()
                    temp.append(node)

                    for e in graph[node]:
                        if e not in visit:
                            stack.append(e)
                            visit.add(e)
                res.append([toName[email]] + sorted(temp))

        return res