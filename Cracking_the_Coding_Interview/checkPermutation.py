# Check Permutation: Given two strings, write a method to decide if one is a permutation of the
# other.

# Solution #1: Sort the strings.

def permutation(s,t):
    if len(s) != len(t):
        return False
    return sorted(s) == sorted(t)

print(permutation('abc df','df bca'))

# Solution #2: Check if the two strings have identical character counts.

def permutation(s,t):
    if len(s) != len(t):
        return False

    char_set = [0] * 128
    s_array = [ord(l) for l in s]

    for n in s_array:
        char_set[n]+=1
    
    for i in range(len(t)):
        c = ord(t[i])
        char_set[c]-=1
        if(char_set[c]<0):
            return False

    return True 


print(permutation('abc dfg sfcc','abc dfg sflc'))