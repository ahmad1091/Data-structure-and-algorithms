# Is Unique: Implement an algorithm to determine if a string has all unique characters. What if you
# cannot use additional data structures?


def isUniqueChars(str):
    if len(str) > 128:
        return False
    
    char_set = [False] * 128

    for i in range(len(str)):
        val = ord(str[i])
        print(str[i],'::',val,char_set[val])
        if char_set[val]:
            return False
        
        char_set[val] = True

    return True

print(isUniqueChars('5dj7g5af4#9'))