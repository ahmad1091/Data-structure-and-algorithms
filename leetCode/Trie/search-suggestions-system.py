# 1268. Search Suggestions System
# #
# You are given an array of strings products and a string searchWord.

# Design a system that suggests at most three product names from products after each character of searchWord is typed. Suggested products should have common prefix with searchWord. If there are more than three products with a common prefix return the three lexicographically minimums products.

# Return a list of lists of the suggested products after each character of searchWord is typed.

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        res = []
        for i in range(len(searchWord)):
            temp = []
            for c in products:
                if searchWord[:i+1] ==  c[:i+1]:
                    temp.append(c)
                if len(temp) == 3:
                    break 
            res.append(temp)

        return res

# sol 2: 
class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        res = []

        l, r = 0, len(products) - 1
        for i in range(len(searchWord)):
            c = searchWord[i]
            
            while (l <= r) and (len(products[l]) <= i or products[l][i] != c):
                l += 1 

            while (l <= r) and (len(products[r]) <= i or products[r][i] != c):
                r -= 1

            res.append([])
            remain = r - l + 1
            for j in range(min(3, remain)):
                res[-1].append(products[l + j])
            
        return res
