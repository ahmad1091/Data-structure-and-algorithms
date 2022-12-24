# Bracket Match
# A string of brackets is considered correctly matched if every opening bracket in the string can be paired up with a later closing bracket, and vice versa. For instance, “(())()” is correctly matched, whereas “)(“ and “((” aren’t. For instance, “((” could become correctly matched by adding two closing brackets at the end, so you’d return 2.

# Given a string that consists of brackets, write a function bracketMatch that takes a bracket string as an input and returns the minimum number of brackets you’d need to add to the input in order to make it correctly matched.

# Explain the correctness of your code, and analyze its time and space complexities.

def bracket_match(text):
  countO = 0
  countC = 0
  for t in text: 
    
    if t == '(':
      countO += 1
      
    else:
      countO -= 1
      
    if countO < 0:
      countO += 1
      countC += 1
          
  return countO + countC

# sol 2:
  function bracketMatch(text):
    diffCounter = 0
    ans = 0
    n = text.length

    for i from 0 to n-1:
        if ( text[i] == '(' ):
            diffCounter += 1
        else if ( text[i] == ')' ):
            diffCounter -= 1
        if ( diffCounter < 0 ):
            diffCounter += 1
            ans += 1

    return ans + diffCounter