from RuleDesign import apply_rules_on_word
import string
import os
import nltk

all_words = []
filtered_word = apply_rules_on_word('Articles')
word_frequency = []


# This function will extract all words from articles
def extractAllWords(folder_name):
    global all_words
    unicode = [b'\\u0a95', b'\\u0a96', b'\\u0a97', b'\\u0a98', b'\\u0a99', b'\\u0a9a', b'\\u0a9b', b'\\u0a9c',
               b'\\u0a9d', b'\\u0a9e', b'\\u0a9f', b'\\u0aa0', b'\\u0aa1', b'\\u0aa2', b'\\u0aa3', b'\\u0aa4',
               b'\\u0aa5', b'\\u0aa6', b'\\u0aa7', b'\\u0aa8', b'\\u0aaa', b'\\u0aab', b'\\u0aac', b'\\u0aad',
               b'\\u0aae', b'\\u0aaf', b'\\u0ab0', b'\\u0ab2', b'\\u0ab3', b'\\u0ab5', b'\\u0ab6', b'\\u0ab7',
               b'\\u0ab8', b'\\u0ab9', b'\\u0a85', b'\\u0a86', b'\\u0a87', b'\\u0a88', b'\\u0a89', b'\\u0a8a',
               b'\\u0a8B']

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
                          #if word not in unique:
                                unique.append([word, len(word)])

            for i in unique:
                count = 0
                for j in unicode:
                    if j in i[0].encode("unicode_escape"):
                        count += 1

                if count > 3:
                    all_words.append(i[0])


extractAllWords('Articles')
print(all_words)
print(len(all_words))
print(filtered_word)
print(len(filtered_word))

# def frequntly_used_word():
#     global all_words
#     all_words_freq = nltk.FreqDist(all_words)
#     print(all_words_freq.most_common(15))
#
# frequntly_used_word()

def find_frequncy():
    global all_words,filtered_word,word_frequency

    for rule_word in filtered_word:
        count = 0
        for article_word in all_words:
            if rule_word == article_word:
                count += 1
        word_frequency.append([count])



find_frequncy()
# word_frequency.sort()
# print(word_frequency[::-1])