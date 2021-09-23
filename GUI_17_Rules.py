import string
import os


# Store words from all the articles
all_words = []
punctuated_word = []
stop_words = []
filter_words = []
matching_word=[]
copy_all_words = []

# Store encoded words
encoded_words = []

# Store Rule words
rule_1_words = []
rule_2_words = []
rule_3_words = []
rule_4_words = []
rule_5_words = []
rule_6_words = []
rule_7_words = []
rule_8_words = []
rule_9_words = []
rule_10_words = []
rule_11_words = []
rule_12_words = []
rule_13_words = []
rule_14_words = []
rule_15_words = []
rule_16_words = []
rule_17_words = []

frequency_list = []
words_above_2_and_bellow_6_letter = []

avg_frequency = 0

# This function will extract all words from articles
def extractAllWords(article):
    global all_words,punctuated_word,frequency_list,avg_frequency
    unicode = [b"'\\u0a95'", b"'\\u0a96'", b"'\\u0a97'", b"'\\u0a98'", b"'\\u0a99'", b"'\\u0a9a'", b"'\\u0a9b'", b"'\\u0a9c'",
               b"'\\u0a9d'", b"'\\u0a9e'", b"'\\u0a9f'", b"'\\u0aa0'", b"'\\u0aa1'", b"'\\u0aa2'", b"'\\u0aa3'", b"'\\u0aa4'",
               b"'\\u0aa5'", b"'\\u0aa6'", b"'\\u0aa7'", b"'\\u0aa8'", b"'\\u0aaa'", b"'\\u0aab'", b"'\\u0aac'", b"'\\u0aad'",
               b"'\\u0aae'", b"'\\u0aaf'", b"'\\u0ab0'", b"'\\u0ab2'", b"'\\u0ab3'", b"'\\u0ab5'", b"'\\u0ab6'", b"'\\u0ab7'",
               b"'\\u0ab8'", b"'\\u0ab9'", b"'\\u0a85'", b"'\\u0a86'", b"'\\u0a87'", b"'\\u0a88'", b"'\\u0a89'", b"'\\u0a8a'",
               b"'\\u0a8b'",b"'\\u0a8c'",b"'\\u0a8d'",b"'\\u0a8f'",b"'\\u0a90'",b"'\\u0a91'",b"'\\u0a93'",b"'\\u0a94'"]

    wordstring = open(article, encoding="utf-8").read()

    wordlist = wordstring.split()

    wordfreq = []
    for w in wordlist:
        wordfreq.append(wordlist.count(w))

    frequency_list = (zip(wordlist, wordfreq))
    avg_frequency=round((max(wordfreq)*10)/100)

    # articlePaths = [os.path.join(folder_name, f) for f in os.listdir(folder_name)]
    # for article in articlePaths:
    file = open(article, 'r', encoding='utf8')
    lines = file.readlines()
    if len(lines) > 1:
        unique = []
        for line in lines:
            words = line.split()
            for word in words:
                flag = 0
                for letter in word:
                    if letter in string.punctuation:
                        if letter == "," or letter == ".":
                            if word[-1] == letter:
                                if word not in punctuated_word:
                                    punctuated_word.append(word)
                        flag = 1
                    if (ord(letter) >= 65 and ord(letter) <= 90) or (ord(letter) >= 97 and ord(letter) <= 122) or (
                            ord(letter) >= 48 and ord(letter) <= 57):
                        flag = 1
                if flag == 0:
                    if len(word) >= 1:
                        if [word,len(word)] not in unique:
                            unique.append([word, len(word)])


        # punctuated_word filter
        for word in punctuated_word:
            flag = 0
            word = word[:-1]
            for letter in word:
                if (ord(letter) >= 65 and ord(letter) <= 90) or (ord(letter) >= 97 and ord(letter) <= 122) or (
                        ord(letter) >= 48 and ord(letter) <= 57):
                    flag = 1
            if flag == 0:
                if len(word) >= 1:
                    if [word, len(word)] not in unique:
                        unique.append([word, len(word)])


        # Filter all words and creating final list of words
        for i in unique:
            count = 0
            for c in i[0]:
                for j in unicode:
                    if j == repr(c).encode("unicode_escape"):
                        count += 1

            if count >= 1:
                all_words.append([i[0],count,len(i[0])])

    # print("----------All Word-----------")
    # print(all_words)
    # print("Step 1: Total Words in article : ",len(all_words))
    # return all_words

# This function will convert all article words(all_words) into unicode
def wordToUnicode():
    global all_words,encoded_words
    for i in all_words:
        count = 0
        temp = []
        for j in i[0]:
            temp.append(j.encode("unicode_escape"))
        encoded_words.append([i, temp])


def rule_1():
    global encoded_words,rule_1_words,frequency_list,avg_frequency
    frequency_list = list(frequency_list)
    unicode = [b'\\u0a95', b'\\u0a96', b'\\u0a97', b'\\u0a98', b'\\u0a99', b'\\u0a9a', b'\\u0a9b',
               b'\\u0a9c', b'\\u0a9d', b'\\u0a9e', b'\\u0a9f', b'\\u0aa0', b'\\u0aa1', b'\\u0aa2', b'\\u0aa3',
               b'\\u0aa4', b'\\u0aa5', b'\\u0aa6', b'\\u0aa7', b'\\u0aa8', b'\\u0aaa', b'\\u0aab', b'\\u0aac',
               b'\\u0aad', b'\\u0aae', b'\\u0aaf', b'\\u0ab0', b'\\u0ab2', b'\\u0ab3', b'\\u0ab5', b'\\u0ab6',
               b'\\u0ab7', b'\\u0ab8', b'\\u0ab9', b'\\u0a85', b'\\u0a86', b'\\u0a87', b'\\u0a88', b'\\u0a89',
               b'\\u0a8a', b'\\u0a8b', b'\\u0a8c', b'\\u0a8d', b'\\u0a8f', b'\\u0a90', b'\\u0a91', b'\\u0a93',
               b'\\u0a94']

    for x in encoded_words:
        # for y in frequency_list:
        #      if x[0][0] == y[0] and y[1] > avg_frequency:
                if x[0][1] == 1:
                     if x[1][-1] in unicode or x[1][0] in unicode:
                        if x[0][0] not in ["માં","ચા","બા","ધી","પી","ગૌ"]:
                            rule_1_words.append(x[0][0])


def rule_2():
    global encoded_words,rule_2_words,frequency_list,avg_frequency
    frequency_list = list(frequency_list)

    for x in encoded_words:
        # for y in frequency_list:
        #      if x[0][0] == y[0] and y[1] > avg_frequency:
                if x[0][1] == 2:
                    if (x[1][-2] == b'\u0aa5' and x[1][-1] == b'\u0ac0'):
                        rule_2_words.append(x[0][0])


def rule_3():
    global encoded_words,rule_3_words,frequency_list,avg_frequency
    frequency_list = list(frequency_list)

    for x in encoded_words:
        # for y in frequency_list:
        #      if x[0][0] == y[0] and y[1] > avg_frequency:
                if x[0][1] == 2:
                    if (x[1][-2] == b'\u0ab5' and x[1][-1] == b'\u0ac1') or (x[1][-2] == b'\u0ab5' and x[1][-1] == b'\u0acb'):
                        rule_3_words.append(x[0][0])


def rule_4():
    global encoded_words,rule_4_words,frequency_list,avg_frequency
    frequency_list = list(frequency_list)

    for x in encoded_words:
        # for y in frequency_list:
        #      if x[0][0] == y[0] and y[1] > avg_frequency:
                if x[0][1] == 2:
                    if (x[1][-2] == b'\u0aa8' and x[1][-1] == b'\u0ac0'):
                        if x[1][1] != b'\u0abe' or x[1][1] != b'\u0abf' or x[1][1] != b'\u0ab0':
                            rule_4_words.append(x[0][0])


def rule_5():
    global encoded_words,rule_5_words,frequency_list,avg_frequency
    frequency_list = list(frequency_list)

    for x in encoded_words:
        # for y in frequency_list:
        #      if x[0][0] == y[0] and y[1] > avg_frequency:
                if x[0][1] == 2:
                    if x[1][-2] == b'\u0aa3' and not(x[1][0] == b'\u0aa5' and x[1][1] == b'\u0abe'):
                        rule_5_words.append(x[0][0])

def rule_6():
    global encoded_words,rule_6_words,frequency_list,avg_frequency
    frequency_list = list(frequency_list)

    for x in encoded_words:
        # for y in frequency_list:
        #      if x[0][0] == y[0] and y[1] > avg_frequency:
                if x[0][1] == 2:
                    if (x[1][-2] == b'\u0aa8' and x[1][-1] == b'\u0ac1') and x[1][1] == b'\u0ac7':
                        rule_6_words.append(x[0][0])

def rule_7():
    global encoded_words,rule_7_words,frequency_list,avg_frequency
    frequency_list = list(frequency_list)

    for x in encoded_words:
        # for y in frequency_list:
        #      if x[0][0] == y[0] and y[1] > avg_frequency:
                if x[0][1] == 2:
                    if x[1][-1] == b'\u0a88' and x[0][2] == 2:
                        rule_7_words.append(x[0][0])
                    if x[1][-1] == b'\u0a88' and x[0][2] == 3:
                        if x[1][1] == b'\u0acb':
                            rule_7_words.append(x[0][0])


def rule_8():
    global encoded_words,rule_8_words,frequency_list,avg_frequency
    frequency_list = list(frequency_list)

    for x in encoded_words:
        # for y in frequency_list:
        #      if x[0][0] == y[0] and y[1] > avg_frequency:
                if x[0][1] == 2:
                    if x[1][0] == b'\u0ab9' and x[1][-2] == b'\u0aa4':
                        #if x[1][1] == b'\u0abf' or x[1][1] == b'\u0ac0':
                            rule_8_words.append(x[0][0])


def rule_9():
    global encoded_words,rule_9_words,frequency_list,avg_frequency
    frequency_list = list(frequency_list)

    for x in encoded_words:
        # for y in frequency_list:
        #      if x[0][0] == y[0] and y[1] > avg_frequency:
                if x[0][1] == 2:
                    if x[1][-2] == b'\u0aa8' and x[1][-1] == b'\u0ac7':
                        rule_9_words.append(x[0][0])


def rule_10():
    global encoded_words,rule_10_words,frequency_list,avg_frequency
    frequency_list = list(frequency_list)

    for x in encoded_words:
        # for y in frequency_list:
        #      if x[0][0] == y[0] and y[1] > avg_frequency:
                if x[0][1] == 2:
                    if x[1][-1] == b'\u0aae':
                        if x[0][2] == 3 and x[1][1] != b'\u0abe':
                            rule_10_words.append(x[0][0])


def rule_11():
    global encoded_words,rule_11_words,frequency_list,avg_frequency
    frequency_list = list(frequency_list)

    for x in encoded_words:
        # for y in frequency_list:
        #      if x[0][0] == y[0] and y[1] > avg_frequency:
                if x[0][1] == 2:
                    if (x[1][-2] == b'\u0aa4' and x[1][-1] == b'\u0acb') or (x[1][-2] == b'\u0aa4' and x[1][-1] == b'\u0ac7'):
                        rule_11_words.append(x[0][0])

def rule_12():
    global encoded_words,rule_12_words,frequency_list,avg_frequency
    frequency_list = list(frequency_list)
    unicode = [b'\\u0a95', b'\\u0a96', b'\\u0a97', b'\\u0a98', b'\\u0a99', b'\\u0a9a', b'\\u0a9b',
               b'\\u0a9c', b'\\u0a9d', b'\\u0a9e', b'\\u0a9f', b'\\u0aa0', b'\\u0aa1', b'\\u0aa2', b'\\u0aa3',
               b'\\u0aa4', b'\\u0aa5', b'\\u0aa6', b'\\u0aa7', b'\\u0aa8', b'\\u0aaa', b'\\u0aab', b'\\u0aac',
               b'\\u0aad', b'\\u0aae', b'\\u0aaf', b'\\u0ab0', b'\\u0ab2', b'\\u0ab3', b'\\u0ab5', b'\\u0ab6',
               b'\\u0ab7', b'\\u0ab8', b'\\u0ab9', b'\\u0a85', b'\\u0a86', b'\\u0a87', b'\\u0a88', b'\\u0a89',
               b'\\u0a8a', b'\\u0a8b', b'\\u0a8c', b'\\u0a8d', b'\\u0a8f', b'\\u0a90', b'\\u0a91', b'\\u0a93',
               b'\\u0a94']


    for x in encoded_words:
        for y in frequency_list:
             if x[0][0] == y[0] and y[1] > avg_frequency:
                 if x[0][1] == 3 or x[0][1] == 4:
                     if x[1][0] in unicode:
                         if x[1][-1] == b'\u0abe' or x[1][-1] == b'\u0acb' or x[1][-1] == b'\u0a9c' or x[1][-1] == b'\u0aa8' or x[1][-1] == b'\u0ab2' or x[1][-1] == b'\u0aa3':
                             rule_12_words.append(x[0][0])
                         if x[1][-1] != b'\u0abe' or x[1][-1] != b'\u0acb' or x[1][-1] != b'\u0a9c' or x[1][-1] != b'\u0aa8' or x[1][-1] != b'\u0ab2' or x[1][-1] != b'\u0aa3':
                             rule_12_words.append(x[0][0])

def rule_13():
    global encoded_words,rule_13_words,frequency_list,avg_frequency
    frequency_list = list(frequency_list)
    unicode = [b'\\u0a95', b'\\u0a96', b'\\u0a97', b'\\u0a98', b'\\u0a99', b'\\u0a9a', b'\\u0a9b',
               b'\\u0a9c', b'\\u0a9d', b'\\u0a9e', b'\\u0a9f', b'\\u0aa0', b'\\u0aa1', b'\\u0aa2', b'\\u0aa3',
               b'\\u0aa4', b'\\u0aa5', b'\\u0aa6', b'\\u0aa7', b'\\u0aa8', b'\\u0aaa', b'\\u0aab', b'\\u0aac',
               b'\\u0aad', b'\\u0aae', b'\\u0aaf', b'\\u0ab0', b'\\u0ab2', b'\\u0ab3', b'\\u0ab5', b'\\u0ab6',
               b'\\u0ab7', b'\\u0ab8', b'\\u0ab9', b'\\u0a85', b'\\u0a86', b'\\u0a87', b'\\u0a88', b'\\u0a89',
               b'\\u0a8a', b'\\u0a8b', b'\\u0a8c', b'\\u0a8d', b'\\u0a8f', b'\\u0a90', b'\\u0a91', b'\\u0a93',
               b'\\u0a94']
    for x in encoded_words:
        for y in frequency_list:
             if x[0][0] == y[0] and y[1] > avg_frequency:
                if x[0][1] == 4 or x[0][1] == 5:
                    if x[1][0] in unicode:
                        if (x[1][-1] == b'\u0abe' or x[1][-1] == b'\u0acb' or x[1][-1] == b'\u0ac0' or x[1][-1] == b'\u0ac7' or x[1][-1] == b'\u0ac1') and (x[1][0] == b'\u0a89' or x[1][0] == b'\u0ab8' or x[1][0] == b'\u0aaa'):
                            rule_13_words.append(x[0][0])
                        if (x[1][-1] != b'\u0abe' or x[1][-1] != b'\u0acb' or x[1][-1] != b'\u0ac0' or x[1][
                            -1] != b'\u0ac7' or x[1][-1] != b'\u0ac1') and (
                                x[1][0] == b'\u0a89' or x[1][0] == b'\u0ab8' or x[1][0] == b'\u0aaa'):
                            rule_13_words.append(x[0][0])

def rule_14():
    global encoded_words,rule_14_words,frequency_list,avg_frequency
    frequency_list = list(frequency_list)
    unicode = [b'\\u0a95', b'\\u0a96', b'\\u0a97', b'\\u0a98', b'\\u0a99', b'\\u0a9a', b'\\u0a9b',
               b'\\u0a9c', b'\\u0a9d', b'\\u0a9e', b'\\u0a9f', b'\\u0aa0', b'\\u0aa1', b'\\u0aa2', b'\\u0aa3',
               b'\\u0aa4', b'\\u0aa5', b'\\u0aa6', b'\\u0aa7', b'\\u0aa8', b'\\u0aaa', b'\\u0aab', b'\\u0aac',
               b'\\u0aad', b'\\u0aae', b'\\u0aaf', b'\\u0ab0', b'\\u0ab2', b'\\u0ab3', b'\\u0ab5', b'\\u0ab6',
               b'\\u0ab7', b'\\u0ab8', b'\\u0ab9', b'\\u0a85', b'\\u0a86', b'\\u0a87', b'\\u0a88', b'\\u0a89',
               b'\\u0a8a', b'\\u0a8b', b'\\u0a8c', b'\\u0a8d', b'\\u0a8f', b'\\u0a90', b'\\u0a91', b'\\u0a93',
               b'\\u0a94']
    for x in encoded_words:
        for y in frequency_list:
             if x[0][0] == y[0] and y[1] > avg_frequency:
                if x[0][1] == 4 or x[0][1] == 5:
                    if x[1][0] in unicode:
                        if (x[1][-2] == b'\u0ab5' and x[1][-1] == b'\u0ac1') or (x[1][-2] == b'\u0ab2' and x[1][-1] == b'\u0ac1'):
                            rule_14_words.append(x[0][0])

def rule_15():
    global encoded_words,rule_15_words,frequency_list,avg_frequency
    frequency_list = list(frequency_list)
    unicode = [b'\\u0a95', b'\\u0a96', b'\\u0a97', b'\\u0a98', b'\\u0a99', b'\\u0a9a', b'\\u0a9b',
               b'\\u0a9c', b'\\u0a9d', b'\\u0a9e', b'\\u0a9f', b'\\u0aa0', b'\\u0aa1', b'\\u0aa2', b'\\u0aa3',
               b'\\u0aa4', b'\\u0aa5', b'\\u0aa6', b'\\u0aa7', b'\\u0aa8', b'\\u0aaa', b'\\u0aab', b'\\u0aac',
               b'\\u0aad', b'\\u0aae', b'\\u0aaf', b'\\u0ab0', b'\\u0ab2', b'\\u0ab3', b'\\u0ab5', b'\\u0ab6',
               b'\\u0ab7', b'\\u0ab8', b'\\u0ab9', b'\\u0a85', b'\\u0a86', b'\\u0a87', b'\\u0a88', b'\\u0a89',
               b'\\u0a8a', b'\\u0a8b', b'\\u0a8c', b'\\u0a8d', b'\\u0a8f', b'\\u0a90', b'\\u0a91', b'\\u0a93',
               b'\\u0a94']
    for x in encoded_words:
        for y in frequency_list:
             if x[0][0] == y[0] and y[1] > avg_frequency:
                if x[0][1] == 3:
                    if x[1][0] in unicode:
                        if (x[1][-2] == b'\u0ab5' and x[1][-1] == b'\u0ac1'):
                            rule_15_words.append(x[0][0])

def rule_16():
    global encoded_words,rule_16_words,frequency_list,avg_frequency
    frequency_list = list(frequency_list)
    unicode = [b'\\u0a95', b'\\u0a96', b'\\u0a97', b'\\u0a98', b'\\u0a99', b'\\u0a9a', b'\\u0a9b',
               b'\\u0a9c', b'\\u0a9d', b'\\u0a9e', b'\\u0a9f', b'\\u0aa0', b'\\u0aa1', b'\\u0aa2', b'\\u0aa3',
               b'\\u0aa4', b'\\u0aa5', b'\\u0aa6', b'\\u0aa7', b'\\u0aa8', b'\\u0aaa', b'\\u0aab', b'\\u0aac',
               b'\\u0aad', b'\\u0aae', b'\\u0aaf', b'\\u0ab0', b'\\u0ab2', b'\\u0ab3', b'\\u0ab5', b'\\u0ab6',
               b'\\u0ab7', b'\\u0ab8', b'\\u0ab9', b'\\u0a85', b'\\u0a86', b'\\u0a87', b'\\u0a88', b'\\u0a89',
               b'\\u0a8a', b'\\u0a8b', b'\\u0a8c', b'\\u0a8d', b'\\u0a8f', b'\\u0a90', b'\\u0a91', b'\\u0a93',
               b'\\u0a94']
    for x in encoded_words:
        for y in frequency_list:
             if x[0][0] == y[0] and y[1] > avg_frequency:
                if x[0][1] > 4:
                    if x[1][0] in unicode:
                        if x[1][-1] == b'\u0abe' or x[1][-1] == b'\u0ac7':
                            rule_16_words.append(x[0][0])

def rule_17():
    global encoded_words,rule_17_words,frequency_list,avg_frequency
    frequency_list = list(frequency_list)
    unicode = [b'\\u0a95', b'\\u0a96', b'\\u0a97', b'\\u0a98', b'\\u0a99', b'\\u0a9a', b'\\u0a9b',
               b'\\u0a9c', b'\\u0a9d', b'\\u0a9e', b'\\u0a9f', b'\\u0aa0', b'\\u0aa1', b'\\u0aa2', b'\\u0aa3',
               b'\\u0aa4', b'\\u0aa5', b'\\u0aa6', b'\\u0aa7', b'\\u0aa8', b'\\u0aaa', b'\\u0aab', b'\\u0aac',
               b'\\u0aad', b'\\u0aae', b'\\u0aaf', b'\\u0ab0', b'\\u0ab2', b'\\u0ab3', b'\\u0ab5', b'\\u0ab6',
               b'\\u0ab7', b'\\u0ab8', b'\\u0ab9', b'\\u0a85', b'\\u0a86', b'\\u0a87', b'\\u0a88', b'\\u0a89',
               b'\\u0a8a', b'\\u0a8b', b'\\u0a8c', b'\\u0a8d', b'\\u0a8f', b'\\u0a90', b'\\u0a91', b'\\u0a93',
               b'\\u0a94']
    for x in encoded_words:
        for y in frequency_list:
             if x[0][0] == y[0] and y[1] > avg_frequency:
                if x[0][1] == 3 or x[0][1] == 4 or x[0][1] == 5:
                    if x[1][0] in unicode:
                        if (x[1][-3] == b'\u0aae' and x[1][-2] == b'\u0abe' and x[1][-1] == b'\u0a82') or (x[1][-2] == b'\u0aa8' and x[1][-1] == b'\u0abe'):
                            rule_17_words.append(x[0][0])


def apply_rules_on_word(article_folder):
    global all_words,encoded_words,rule_1_words,rule_2_words,rule_3_words,rule_4_words,rule_5_words,rule_6_words,rule_7_words,rule_8_words,rule_9_words,rule_10_words,rule_11_words,copy_all_words,rule_12_words,rule_13_words,rule_14_words,rule_15_words,rule_16_words,rule_17_words
    extractAllWords(article_folder)

    wordToUnicode()
    rule_1()
    rule_2()
    rule_3()
    rule_4()
    rule_5()
    rule_6()
    rule_7()
    rule_8()
    rule_9()
    rule_10()
    rule_11()
    rule_12()
    rule_13()
    rule_14()
    rule_15()
    rule_16()
    rule_17()
    # print('Rule 1', rule_1_words)
    # print('Rule 2', rule_2_words)
    # print('Rule 3', rule_3_words)
    # print('Rule 4', rule_4_words)
    # print('Rule 5', rule_5_words)
    # print('Rule 6', rule_6_words)
    # print('Rule 7', rule_7_words)
    # print('Rule 8', rule_8_words)
    # print('Rule 9', rule_9_words)
    # print('Rule 10', rule_10_words)
    # print('Rule 11', rule_11_words)
    # print('Rule 12', rule_12_words)
    # print('Rule 13', rule_13_words)
    # print('Rule 14', rule_14_words)
    # print('Rule 15', rule_15_words)
    # print('Rule 16', rule_16_words)
    # print('Rule 17', rule_17_words)
    filter_words = []
    for word in rule_1_words:
        if word not in filter_words:
            filter_words.append(word)
    for word in rule_2_words:
        if word not in filter_words:
            filter_words.append(word)
    for word in rule_3_words:
        if word not in filter_words:
            filter_words.append(word)
    for word in rule_4_words:
        if word not in filter_words:
            filter_words.append(word)
    for word in rule_5_words:
        if word not in filter_words:
            filter_words.append(word)
    for word in rule_6_words:
        if word not in filter_words:
            filter_words.append(word)
    for word in rule_7_words:
        if word not in filter_words:
            filter_words.append(word)
    for word in rule_8_words:
        if word not in filter_words:
            filter_words.append(word)
    for word in rule_9_words:
        if word not in filter_words:
            filter_words.append(word)
    for word in rule_10_words:
        if word not in filter_words:
            filter_words.append(word)
    for word in rule_11_words:
        if word not in filter_words:
            filter_words.append(word)
    for word in rule_12_words:
        if word not in filter_words:
            filter_words.append(word)
    for word in rule_13_words:
        if word not in filter_words:
            filter_words.append(word)
    for word in rule_14_words:
        if word not in filter_words:
            filter_words.append(word)
    for word in rule_15_words:
        if word not in filter_words:
            filter_words.append(word)
    for word in rule_16_words:
        if word not in filter_words:
            filter_words.append(word)
    for word in rule_17_words:
        if word not in filter_words:
            filter_words.append(word)
    copy_all_words = all_words
    all_words = []
    encoded_words = []
    rule_1_words = []
    rule_2_words = []
    rule_3_words = []
    rule_4_words = []
    rule_5_words = []
    rule_6_words = []
    rule_7_words = []
    rule_8_words = []
    rule_9_words = []
    rule_10_words = []
    rule_11_words = []
    rule_12_words = []
    rule_13_words = []
    rule_14_words = []
    rule_15_words = []
    rule_16_words = []
    rule_17_words = []

    new_file_data = []

    wordstring = open(article_folder, encoding="utf-8").read()

    wordlist = wordstring.split()
    # print(wordlist)

    for a in wordlist:
        if a not in filter_words:
            new_file_data.append(a)

    new_file_data_plain_text = ' '.join(new_file_data)

    newfile = open('Output/result.txt',"w",encoding="utf-8").write(new_file_data_plain_text)

    # print(new_file_data)
    # print(len(new_file_data))
    return len(new_file_data)
# apply_rules_on_word("D:/Python Projects/Stop Word/Articles/1.txt")