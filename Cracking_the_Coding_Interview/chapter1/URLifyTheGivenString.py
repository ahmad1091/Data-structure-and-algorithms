# URLify: Write a method to replace all spaces in a string with '%20: You may assume that the string
# has sufficient space at the end to hold the additional characters, and that you are given the "true"
# length of the string. (Note: If implementing in Java, please use a character array so that you can
# perform this operation in place.)
# EXAMPLE
# Input: "Mr John Smith   ",13
# Output: "Mr%20J ohn%20Smith"

def replaceSpaces(str,trueLength):
    splittedStr = list(str)
    print(splittedStr.append(''))
    spaceCount, index = 0, 0
    for i in range(trueLength):
        if splittedStr[i] == ' ':
            spaceCount+=1

    if (trueLength < len(splittedStr)):
        splittedStr[trueLength] = '\0'
    index = trueLength + spaceCount * 2
    
    for i in range(trueLength-1,-1,-1):
        if splittedStr[i] == ' ':
            splittedStr[index -1 ] = '0'
            splittedStr[index -2 ] = '2'
            splittedStr[index -3 ] = '%'
            index -= 3
        else:
            print(i,index-1)
            print(splittedStr[index - 1] , splittedStr[i])
            splittedStr[index - 1] = splittedStr[i]
            index -= 1
    print(splittedStr)

    
    
replaceSpaces("Mr John Smith   ",13)