# Palindrome Permutation: Given a string, write a function to check if it is a permutation of
# a palindrome. A palindrome is a word or phrase that is the same forwards and backwards. A
# permutation is a rearrangement of letters. The palindrome does not need to be limited to just
# dictionary words.
# EXAMPLE
# Input: Tact Coa
# Output: True (permutations:"taco cat'; "atco cta '; etc.)

# Solution #1: This algorithm takes O(N) time, where N is the length of the string.

# Map each character to a number. a -> 0 , b -> I, C -> 2, etc.

# This is case insensitive. Non-letter characters map to -1. 

def getCharNumber(c):
    a = ord('a')
    z = ord('z')
    val = ord(c)

    if(a <= val and z >= val):
        return val - a
        
    return -1

def buildCharFrequencyTable(phrase):
    char_table = [0]*26
    lower_phrase = phrase.lower()
    for i in range(len(phrase)):
        x = getCharNumber(lower_phrase[i])

        if x != -1 :
            char_table[x] += 1

    return char_table

def checkMaxOneOdd(table):
    foundOdd = False

    for l in table:
        if l % 2 == 1:
            if foundOdd:
                return False
            foundOdd =True
    return True

def isPermutationOfPalindrome(phrase):
    table = buildCharFrequencyTable(phrase)
    return checkMaxOneOdd(table)


# print(isPermutationOfPalindrome('Tact Coa'))

# Solution 2:

def toggle(bitVector,index):
    if (index < 0):
        return bitVector
    mask = 1 << index
    print(index ,mask)
    print(bitVector , mask,'bitVector and mask',bitVector & mask)
    if (bitVector & mask) == 0:
        bitVector= bitVector | mask
    else:
        bitVector = bitVector & ~mask
        print('bitVector &= ! mask',bitVector)
    return bitVector

def createBitVector(phrase):
    bitVector = 0
    for c in phrase:
        x = getCharNumber(c)
        bitVector = toggle(bitVector, x)

    return bitVector

def checkExactlyOneBitSet(bitVector):
    return (bitVector & (bitVector - 1)) == 0

def isPermutationOfPalindrome(phrase):
    bitVector = createBitVector(phrase)
    return bitVector == 0 or checkExactlyOneBitSet(bitVector)

print(isPermutationOfPalindrome('tact coa'))
