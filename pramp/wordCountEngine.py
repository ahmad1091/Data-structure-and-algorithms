# Word Count Engine

# Implement a document scanning function wordCountEngine, which receives a string document and returns a list of all unique words in it and their number of occurrences, sorted by the number of occurrences in a descending order. If two or more words have the same count, they should be sorted according to their order in the original sentence. Assume that all letters are in english alphabet. You function should be case-insensitive, so for instance, the words “Perfect” and “perfect” should be considered the same word.

# The engine should strip out punctuation (even in the middle of a word) and use whitespaces to separate words.

# Analyze the time and space complexities of your solution. Try to optimize for time while keeping a polynomial space complexity.

def word_count_engine(document):
    for i in document:
        if i in ".,;!?":
            document = document.replace(i,' ')

    splitted = document.split()
    wordHash = {}
  
    for i in range(len(splitted)):
        if splitted[i] in wordHash:
            wordHash[splitted[i].lower()] += 1
        else:
            wordHash[splitted[i].lower()] = 1
    result = []
    for i in wordHash:
        result.append([i,wordHash[i]])
    return result.sort(key = lambda result: result[1])

word_count_engine("Practice makes perfect. you'll only get Perfect by practice. just practice!")

# standard sol
function wordCountEngine(document):
    wordMap = new Map()
    wordList = document.split()
    largestCount = 0;

    for i from 0 to wordList.length-1:
        # convert each token to lowercase
        word = wordList[i].toLowerCase()

        # and remove special/punctuation characters
        charArray = []
        for ch in word:
            if (ch >= 'a' and ch <= 'z'):
                charArray.push(ch)

        # form a string from the characters in charArray.
        # use your programming language's native “join”
        # or equivalent function. If there isn't any,
        # implement yourself. It's quite straightforward.
        cleanWord = join(charArray)

        # if the token consisted of only whitespace
        # characters, then cleanWord is an empty string
        # and we should ignore it and continue to the
        # next word.
        if (cleanWord.length < 1):
            continue

        # add clean word to the wordMap and
        # increase counter if needed
        count = 0
        if (cleanWord in wordMap):
            count = wordMap[cleanWord]
            count++
        else:
            count = 1

        if (count > largestCount):
            largestCount = count

        wordMap[cleanWord] = count

    # init the word counter list of lists.
    # Since, in the worst case scenario, the
    # number of lists is going to be as
    # big as the maximum occurrence count,
    # we need counterList's size to be the
    # same to be able to store these lists.
    # Creating counterList will allow us to
    # “bucket-sort” the list by word occurrences
    counterList = new Array(largestCount+1)
    for j from 0 to largestCount:
        counterList[j] = null

    # add all words to a list indexed by the
    # corresponding occurrence number.
    for word in wordMap.keys():
        counter = wordMap[word]
        wordCounterList = counterList[counter]

        if (wordCounterList == null):
            wordCounterList = []

        wordCounterList.push(word)
        counterList[counter] = wordCounterList

    # iterate through the list in reverse order
    # and add only non-null values to result
    result = []
    for l from counterList.length-1 to 0:
        wordCounterList = counterList[l]
        if (wordCounterList == null):
            continue

        stringifiedOccurrenceVal = toString(l)
        for m from 0 to wordCounterList.length-1:
            result.push([wordCounterList[m], stringifiedOccurrenceVal])

    return result