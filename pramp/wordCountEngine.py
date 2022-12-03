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
    return result

word_count_engine("Practice makes perfect. you'll only get Perfect by practice. just practice!")