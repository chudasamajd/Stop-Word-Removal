import string
import os

# Rule 1 and 6 give high accuracy

# Store words from all the articles
all_words = []

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

# This function will extract all words from articles
def extractAllWords(folder_name):
    global all_words
    unicode = [b"'\\u0a95'", b"'\\u0a96'", b"'\\u0a97'", b"'\\u0a98'", b"'\\u0a99'", b"'\\u0a9a'", b"'\\u0a9b'", b"'\\u0a9c'",
               b"'\\u0a9d'", b"'\\u0a9e'", b"'\\u0a9f'", b"'\\u0aa0'", b"'\\u0aa1'", b"'\\u0aa2'", b"'\\u0aa3'", b"'\\u0aa4'",
               b"'\\u0aa5'", b"'\\u0aa6'", b"'\\u0aa7'", b"'\\u0aa8'", b"'\\u0aaa'", b"'\\u0aab'", b"'\\u0aac'", b"'\\u0aad'",
               b"'\\u0aae'", b"'\\u0aaf'", b"'\\u0ab0'", b"'\\u0ab2'", b"'\\u0ab3'", b"'\\u0ab5'", b"'\\u0ab6'", b"'\\u0ab7'",
               b"'\\u0ab8'", b"'\\u0ab9'", b"'\\u0a85'", b"'\\u0a86'", b"'\\u0a87'", b"'\\u0a88'", b"'\\u0a89'", b"'\\u0a8a'",
               b"'\\u0a8b'",b"'\\u0a8c'",b"'\\u0a8d'",b"'\\u0a8f'",b"'\\u0a90'",b"'\\u0a91'",b"'\\u0a93'",b"'\\u0a94'"]

    articlePaths = [os.path.join(folder_name, f) for f in os.listdir(folder_name)]
    for article in articlePaths:
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
                            flag = 1
                    if not (word.isalpha()) and flag == 0:
                        if len(word) > 3:
                            if [word,len(word)] not in unique:
                                unique.append([word, len(word)])

            for i in unique:
                count = 0
                for c in i[0]:
                    for j in unicode:
                        if j == repr(c).encode("unicode_escape"):
                            count += 1

                if count > 3:
                    all_words.append(i[0])

    # print("All Words from Article")
    # print(all_words)
    # print("Total Words : ",len(all_words))
    # print("-----------------")


# This function will convert all article words(all_words) into unicode
def wordToUnicode():
    global all_words,encoded_words
    for i in all_words:
        count = 0
        temp = []
        for j in i:
            temp.append(j.encode("unicode_escape"))
        encoded_words.append([i, temp])

    # print("Encoded Words")
    # print(encoded_words)
    # print("-----------------")


# This rules is based on Dependent vowel signs
# Words that ends with this signs
# e.g. ા, િ, ી, ો, ૌ,  ે,  ૈ
def rule_1():
    global encoded_words,rule_1_words

    rules_code = [b'\u0abe',b'\u0abf',b'\u0ac0',b'\u0acb',b'\u0acc',b'\u0ac7',b'\u0ac8']
    for x in encoded_words:
        if x[1][-1] in rules_code:
            rule_1_words.append(x[0])

    # print("Rule 1 Words")
    # print(rule_1_words)
    # print("Total Words : ",len(rule_1_words))
    # print("-----------------")


# This rules is based on words that ends with ના or માં
def rule_2():
    global encoded_words,rule_2_words

    for x in encoded_words:
        if (x[1][-2] == b'\u0aa8' and x[1][-1] == b'\u0abe') or (x[1][-3] == b'\u0aae' and x[1][-2] == b'\u0abe' and x[1][-1] == b'\u0a82'):
            rule_2_words.append(x[0])

    # print("Rule 2 Words")
    # print(rule_2_words)
    # print("Total Words : ",len(rule_2_words))
    # print("-----------------")


# This rules is based on Independent vowels
# Word that starts with this vowels
# e.g. અ, આ, ઇ, ઈ, ઉ, ઊ, ઋ, ઌ
def rule_3():
    global encoded_words,rule_3_words

    rules_code = [b'\u0a85',b'\u0a86',b'\u0a87',b'\u0a88',b'\u0a89',b'\u0a8a',b'\u0a8b',b'\u0a8c']
    for x in encoded_words:
        if x[1][0] in rules_code:
            rule_3_words.append(x[0])

    # print("Rule 3 Words")
    # print(rule_3_words)
    # print("Total Words : ",len(rule_3_words))
    # print("-----------------")

# This rules is based on words that ends with માંના
def rule_4():
    global encoded_words,rule_4_words

    for x in encoded_words:
        if x[1][-5] == b'\u0aae' and x[1][-4] == b'\u0abe' and x[1][-3] == b'\u0a82' and x[1][-2] == b'\u0aa8' and x[1][-1] == b'\u0abe':
            rule_4_words.append(x[0])

    # print("Rule 4 Words")
    # print(rule_4_words)
    # print("Total Words : ",len(rule_4_words))
    # print("-----------------")


# This rules is based on words that starts with Consonant and end with Dependent vowel signs
def rule_5():
    global encoded_words,rule_5_words
    consonant = [b'\\u0a95', b'\\u0a96', b'\\u0a97', b'\\u0a98', b'\\u0a99', b'\\u0a9a', b'\\u0a9b', b'\\u0a9c',
               b'\\u0a9d', b'\\u0a9e', b'\\u0a9f', b'\\u0aa0', b'\\u0aa1', b'\\u0aa2', b'\\u0aa3', b'\\u0aa4',
               b'\\u0aa5', b'\\u0aa6', b'\\u0aa7', b'\\u0aa8', b'\\u0aaa', b'\\u0aab', b'\\u0aac', b'\\u0aad',
               b'\\u0aae', b'\\u0aaf', b'\\u0ab0', b'\\u0ab2', b'\\u0ab3', b'\\u0ab5', b'\\u0ab6', b'\\u0ab7',
               b'\\u0ab8', b'\\u0ab9']

    rules_code = [b'\u0abe', b'\u0abf', b'\u0ac0', b'\u0acb', b'\u0acc', b'\u0ac7', b'\u0ac8']

    for x in encoded_words:
        if x[1][0] in consonant and x[1][-1] in rules_code:
            rule_5_words.append(x[0])

    # print("Rule 5 Words")
    # print(rule_5_words)
    # print("Total Words : ",len(rule_5_words))
    # print("-----------------")


# This rules is based on Dependent vowel signs, Various Signs
# Words that not ends with this signs
# e.g. ા, િ, ી, ો, ૌ,  ે,  ૈ,  ુ,  ૂ,  ૃ,  ૄ,  ૅ , ૉ,  ઁ ,  ં, ઃ
def rule_6():
    global encoded_words,rule_6_words

    rules_code = [b'\u0abe', b'\u0abf', b'\u0ac0', b'\u0ac1', b'\u0ac2',b'\u0ac3',b'\u0ac4',b'\u0ac5',b'\u0ac7',b'\u0ac8',b'\u0ac9', b'\u0acb', b'\u0acc', b'\u0a81', b'\u0a82', b'\u0a83']
    for x in encoded_words:
        if x[1][-1] not in rules_code:
            rule_6_words.append(x[0])


    # print("Rule 6 Words")
    # print(rule_6_words)
    # print("Total Words : ",len(rule_6_words))
    # print("-----------------")

# This rules is based on Various Signs
# Words that ends with this signs
# e.g.  ઁ ,  ં, ઃ
def rule_7():
    global encoded_words,rule_7_words

    rules_code = [b'\u0a81', b'\u0a82', b'\u0a83']
    for x in encoded_words:
        if x[1][-1] in rules_code:
            rule_7_words.append(x[0])


    # print("Rule 7 Words")
    # print(rule_7_words)
    # print("Total Words : ",len(rule_7_words))
    # print("-----------------")







def apply_rules_on_word(article_folder):
    extractAllWords(article_folder)
    wordToUnicode()
    rule_1()
    rule_2()
    rule_3()
    # rule_4()
    # rule_5()
    rule_6()
    rule_7()
    #rule_8()
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
    return filter_words

# extractAllWords('New Articles')
# wordToUnicode()
# rule_8()

# a = apply_rules_on_word('New Articles')
# print(a)
# print(len(a))

