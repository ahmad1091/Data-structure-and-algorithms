# Decode Variations
# A letter can be encoded to a number in the following way:

# 'A' -> '1', 'B' -> '2', 'C' -> '3', ..., 'Z' -> '26'
# A message is a string of uppercase letters, and it is encoded first using this scheme. For example, 'AZB' -> '1262'

# Given a string of digits S from 0-9 representing an encoded message, return the number of ways to decode it.
# Sol 1:
def decodeVariations(S):
	"""
	@param S: str
	@return: int
	"""
    dp = { len(s) : 1 }
        
    def dfs(i):
        if i in dp:
            return dp[i]
        if s[i] == '0' :
            return 0
        res = dfs(i+1)
            
        if(i+1 < len(s) and (s[i] =='1' or s[i] == '2' and s[i+1] in '0123456')):
            res += dfs(i+2)
                
        dp[i] = res 
        return res 
        
    return dfs(0)

# Sol 2:
def decodeVariations(S):
	"""
	@param S: str
	@return: int
	"""
def decodeVariations(S):
	"""
	@param S: str
	@return: int
	"""
    dp = { len(s) : 1 }
        
    for i in range(len(s)-1 ,-1 ,-1):
        if s[i] == '0':
                dp[i] = 0
        else:
            dp[i] = dp[i+1]
                
        if i+1 < len(s) and (s[i] == '1' or s[i] == '2' and s[i+1] in '0123456'):
            dp[i]+= dp[i+2]
        
    return dp[0]