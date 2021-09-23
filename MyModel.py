import string
import nltk

def loadArticle():
    file = open('Test_article.txt', 'r', encoding="utf8")
    lines = file.readlines()

    unique = []
    for line in lines:
        words = line.split()
        for word in words:
            flag = 0
            for letter in word:
                if letter in string.punctuation:
                    flag = 1
            if not (word.isalpha()) and flag == 0:
                if len(word) > 3:
                    if word[0] + word[-2] + str(len(word)) not in unique:
                        unique.append(word[0] + word[-1] + str(len(word)))

    return unique


def loadStopWord():
    stopwords = open('Gujarati_stopwords_new.txt', 'r', encoding="utf8")
    lines = stopwords.readlines()

    unique = []
    for line in lines:
        words = line.split()
        for word in words:
            flag = 0
            for letter in word:
                if letter in string.punctuation:
                    flag = 1
            if not (word.isalpha()) and flag == 0:
                if len(word) > 1:
                    if line[0] + line[-2] + str(len(word)) not in unique:
                        unique.append(line[0] + line[-2] + str(len(word)))
    return unique


def compareWord(articleWord,stopword):
    result = []
    for word in articleWord:
        for word2 in stopword:
            if word[:2] == word2[:2]:
                result.append(word[:2])

    frequency_words = nltk.FreqDist(result)
    print(frequency_words.most_common(15))

# a = loadArticle()
# b = loadStopWord()
# compareWord(a,b)

def matchCompleteWord():
    file = open('Test_article.txt', 'r', encoding="utf8")
    lines = file.readlines()

    unique = []
    for line in lines:
        words = line.split()
        for word in words:
            flag = 0
            for letter in word:
                if letter in string.punctuation:
                    flag = 1
            if not (word.isalpha()) and flag == 0:
                if len(word) > 3:
                    #if word + str(len(word)) not in unique:
                        unique.append([word , len(word)])

    stopwords = open('Gujarati_stopwords_new.txt', 'r', encoding="utf8")
    lines = stopwords.readlines()

    unique2 = []
    for line in lines:
        words = line.split()
        for word in words:
            flag = 0
            for letter in word:
                if letter in string.punctuation:
                    flag = 1
            if not (word.isalpha()) and flag == 0:
                if len(word) > 1:
                    #if line[0] + line[-2] + str(len(word)) not in unique2:
                        if [word,len(word)] not in unique2:
                            unique2.append([word ,len(word)])

    print('\nArticle Words : \n', unique)
    print('\nLength of Article Words : \n', len(unique))
    print('\nStop Words : \n', unique2)
    print('\nLength of Stop Words : \n', len(unique2))

    print("\n Match with 1st and last letter:\n")
    result = []
    count1 = 0
    for word in unique:
        # print(word[0][0]+word[0][-1])
        for word2 in unique2:
             if word[0][0]+word[0][-1] == word2[0][0]+word2[0][-1]:
                 count1 += 1
                 print(word,"=",word2)
                 if word[0][0]+word[0][-1] not in result:
                    result.append(word[0][0]+word[0][-1])
    print("\nTotal Matching :",count1)
    print('\nRule based on 1st and last letter:')
    print(result)

    print("\n Match with 1st and last letter and length:\n")
    result = []
    count2 = 0
    for word in unique:
        # print(word[0][0]+word[0][-1])
        for word2 in unique2:
            if word[0][0] + word[0][-1] == word2[0][0] + word2[0][-1] and word[1]==word2[1]:
                count2 += 1
                print(word, "=", word2)
                if [word[0][0] + word[0][-1],word[1]] not in result:
                    result.append([word[0][0] + word[0][-1],word[1]])
    print("\nTotal Matching :", count2)
    print('\nRule based on 1st and last letter and Length:')
    print(result)

matchCompleteWord()