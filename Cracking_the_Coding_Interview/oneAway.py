# One Away: There are three types of edits that can be performed on strings: insert a character,
# remove a character, or replace a character. Given two strings, write a function to check if they are
# one edit (or zero edits) away.
# EXAMPLE
# pale, ple -> true
# pales. pale -> true
# pale. bale -> true
# pale. bake -> false
# This algorithm (and almost any reasonable algorithm) takes 0 (n) time, where n is the length of the shorter
# string.
def oneEditReplace(s1, s2):
    foundDifference = False
    for i in range(len(s1)):
        if(s1[i] != s2[i]):
            if(foundDifference):
                return False
        foundDifference = True
    return True

def oneEditInsert(s1,s2):
    i = 0
    j = 0
    while(i < len(s1) and j < len(s2)):
        if(s1[i] != s2[j]):
            if i != j :
                return False
            i += 1
        else:
            i += 1
            j += 1
    return True
            
            



def oneEditAway(s,t):
    if len(s) == len(t):
        return oneEditReplace(s,t)
    elif len(s) - 1 == len(t):
        return oneEditInsert(s,t)
    elif len(s) + 1 == len(t):
        return oneEditInsert(t,s)
    return False

print(oneEditAway('pale','bake'))

