import string
import os
from PyQt5.QtWidgets import QApplication, QWidget, QTableWidget, QTableWidgetItem,QVBoxLayout,QAbstractItemView
import sys
from PyQt5 import QtGui

# Article Name |  Total Word in Article |  Total Word in Article (>5 letters)  |  Word match with stopwords


all_words = []
filtered_word2 = []
matching_word = []
stop_words = []
punctuated_word = []
words_above_5_letter = []
data_for_table = []

# This function will extract all words from Article file
def extractAllWords(article):
    global all_words,punctuated_word
    unicode = [b"'\\u0a95'", b"'\\u0a96'", b"'\\u0a97'", b"'\\u0a98'", b"'\\u0a99'", b"'\\u0a9a'", b"'\\u0a9b'", b"'\\u0a9c'",
               b"'\\u0a9d'", b"'\\u0a9e'", b"'\\u0a9f'", b"'\\u0aa0'", b"'\\u0aa1'", b"'\\u0aa2'", b"'\\u0aa3'", b"'\\u0aa4'",
               b"'\\u0aa5'", b"'\\u0aa6'", b"'\\u0aa7'", b"'\\u0aa8'", b"'\\u0aaa'", b"'\\u0aab'", b"'\\u0aac'", b"'\\u0aad'",
               b"'\\u0aae'", b"'\\u0aaf'", b"'\\u0ab0'", b"'\\u0ab2'", b"'\\u0ab3'", b"'\\u0ab5'", b"'\\u0ab6'", b"'\\u0ab7'",
               b"'\\u0ab8'", b"'\\u0ab9'", b"'\\u0a85'", b"'\\u0a86'", b"'\\u0a87'", b"'\\u0a88'", b"'\\u0a89'", b"'\\u0a8a'",
               b"'\\u0a8b'",b"'\\u0a8c'",b"'\\u0a8d'",b"'\\u0a8f'",b"'\\u0a90'",b"'\\u0a91'",b"'\\u0a93'",b"'\\u0a94'"]

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
                    if (ord(letter) >= 65 and ord(letter) <= 90) or (ord(letter) >= 97 and ord(letter) <= 122) or (ord(letter) >= 48 and ord(letter) <= 57):
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

        for i in unique:
            count = 0
            for c in i[0]:
                for j in unicode:
                    if j == repr(c).encode("unicode_escape"):
                        count += 1

            if count >= 1:
                all_words.append([i[0],count])
    # print("----------All Word--------")
    # print(all_words)
    return len(all_words)

# This function will extract all words from stopword file
def extractAllWordsStopWord(stopwordfolder):
    global stop_words
    unicode = [b"'\\u0a95'", b"'\\u0a96'", b"'\\u0a97'", b"'\\u0a98'", b"'\\u0a99'", b"'\\u0a9a'", b"'\\u0a9b'", b"'\\u0a9c'",
               b"'\\u0a9d'", b"'\\u0a9e'", b"'\\u0a9f'", b"'\\u0aa0'", b"'\\u0aa1'", b"'\\u0aa2'", b"'\\u0aa3'", b"'\\u0aa4'",
               b"'\\u0aa5'", b"'\\u0aa6'", b"'\\u0aa7'", b"'\\u0aa8'", b"'\\u0aaa'", b"'\\u0aab'", b"'\\u0aac'", b"'\\u0aad'",
               b"'\\u0aae'", b"'\\u0aaf'", b"'\\u0ab0'", b"'\\u0ab2'", b"'\\u0ab3'", b"'\\u0ab5'", b"'\\u0ab6'", b"'\\u0ab7'",
               b"'\\u0ab8'", b"'\\u0ab9'", b"'\\u0a85'", b"'\\u0a86'", b"'\\u0a87'", b"'\\u0a88'", b"'\\u0a89'", b"'\\u0a8a'",
               b"'\\u0a8b'",b"'\\u0a8c'",b"'\\u0a8d'",b"'\\u0a8f'",b"'\\u0a90'",b"'\\u0a91'",b"'\\u0a93'",b"'\\u0a94'"]

    articlePaths = [os.path.join(stopwordfolder, f) for f in os.listdir(stopwordfolder)]
    for article in articlePaths:
        file = open(article, 'r', encoding='utf8')
        lines = file.readlines()
        if len(lines) > 1:
            unique = []
            for line in lines:
                line = line[:-1]
                words = line.split()
                for word in words:
                    flag = 0
                    for letter in word:
                        if letter in string.punctuation:
                            flag = 1
                        if (ord(letter) >= 65 and ord(letter) <= 90) or (ord(letter) >= 97 and ord(letter) <= 122) or (
                                ord(letter) >= 48 and ord(letter) <= 57):
                            flag = 1
                    if flag == 0:
                        if len(word) >= 1:
                            if [word,len(word)] not in unique:
                                unique.append([word, len(word)])

            for i in unique:
                count = 0
                for c in i[0]:
                    for j in unicode:
                        if j == repr(c).encode("unicode_escape"):
                            count += 1

                if count >= 1:
                    stop_words.append(i[0])
    # print(stop_words)
    return len(stop_words)

def find_word_with_above_5_letter():
    global all_words,words_above_5_letter
    total_word = 0
    for i in all_words:
        if i[1] > 5:
            words_above_5_letter.append(i[0])
            total_word += 1

    return total_word


def find_matching_word():
    global all_words,stop_words,filtered_word2,matching_word,words_above_5_letter

    for article_word in words_above_5_letter:
        for stop_word in stop_words:
            if article_word == stop_word:
                if article_word not in matching_word:
                    matching_word.append(article_word)
    # print("--------Matching Stop Word------------")
    # print(matching_word)
    return len(matching_word)

def main(folder_name,stop_word_folder):
    global all_words,stop_words,matching_word,data_for_table,words_above_5_letter
    articlePaths = [os.path.join(folder_name, f) for f in os.listdir(folder_name)]

    no_of_article = 0
    for article in articlePaths:
        file = open(article, 'r', encoding='utf8')
        lines = file.readlines()
        if len(lines) > 1 and no_of_article < 11:
            # print("-----------",article,"------------")
            article_word_file = extractAllWords(article)
            # print('Total Word in Article: ',article_word_file)
            extractAllWordsStopWord(stop_word_folder)
            article_word_with_above_5_letters = find_word_with_above_5_letter()
            # print('Total Word in Article with >5 letters :',article_word_with_above_5_letters)
            word_match_with_stop_word = find_matching_word()
            # print('Total Word match with stop word :',word_match_with_stop_word)
            data_for_table.append([article,article_word_file,article_word_with_above_5_letters,word_match_with_stop_word])
            all_words = []
            stop_words = []
            matching_word = []
            words_above_5_letter = []
            no_of_article += 1



class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.title = "Accuracy Table For >5 Letters word"
        self.left = 0
        self.top = 0
        self.width = 1920
        self.height = 1080
        self.InitUI()

    def InitUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left,self.top,self.width,self.height)
        main('Testing','Stopword2')
        self.creatingTables()

        self.show()

    def creatingTables(self):
        vbox = QVBoxLayout()

        tableWidget = QTableWidget()
        tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        tableWidget.setRowCount(11)
        tableWidget.setColumnCount(4)

        tableWidget.setItem(0, 0, QTableWidgetItem("Article Name"))
        tableWidget.setItem(0, 1,QTableWidgetItem("Total Words In Article"))
        tableWidget.setItem(0, 2, QTableWidgetItem(">5 Letters Words In Article"))
        tableWidget.setItem(0, 3, QTableWidgetItem("Word Match with Stop Word"))


        count = 1
        for i in data_for_table:
            # if (round(i[3]/i[2]*100,2) > 70 and round(i[3]/i[2]*100,2) <= 100):
                tableWidget.setItem(count, 0, QTableWidgetItem(i[0]))
                tableWidget.setItem(count, 1, QTableWidgetItem(str(i[1])))
                tableWidget.setItem(count, 2, QTableWidgetItem(str(i[2])))
                tableWidget.setItem(count, 3, QTableWidgetItem(str(i[3])))

                count += 1

        vbox.addWidget(tableWidget)
        self.setLayout(vbox)



App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())
