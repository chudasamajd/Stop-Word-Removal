from RuleDesignForAccuracyTableFor4Letters import apply_rules_on_word as letter4_rules
from RuleDesignForAccuracyTableFor3Letters import apply_rules_on_word as letter3_rules
from RuleDesignForAccuracyTableFor2Letters import apply_rules_on_word as letter2_rules
from NewRules import apply_rules_on_word
import string
import os

from PyQt5.QtWidgets import QApplication, QWidget, QTableWidget, QTableWidgetItem,QVBoxLayout,QAbstractItemView
import sys
from PyQt5 import QtGui

all_words = []
filtered_word2 = []
matching_word = []
stop_words = []

data_for_table = []

# This function will extract all words from Article file
def extractAllWords(article):
    global all_words
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
                        flag = 1
                    if (ord(letter) >= 65 and ord(letter) <= 90) or (ord(letter) >= 97 and ord(letter) <= 122) or (ord(letter) >= 48 and ord(letter) <= 57):
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
                all_words.append(i[0])
    #print(all_words)
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


def find_matching_word():
    global all_words,stop_words,filtered_word2,matching_word

    for article_word in all_words:
        for stop_word in stop_words:
            if article_word == stop_word:
                if article_word not in matching_word:
                    matching_word.append(article_word)
    # print("-----Article word match with Stop word File------")
    # print(matching_word)
    # print(len(matching_word))
    # print("-------------------------------------")
    return len(matching_word)

def main(folder_name,stop_word_folder):
    global all_words,stop_words,matching_word,data_for_table
    articlePaths = [os.path.join(folder_name, f) for f in os.listdir(folder_name)]

    for article in articlePaths:
        file = open(article, 'r', encoding='utf8')
        lines = file.readlines()
        if len(lines) > 1:
            # print("-----------",article,"------------")
            article_word_file = extractAllWords(article)
            stop_word_file = extractAllWordsStopWord(stop_word_folder)
            # print(stop_word_file)
            #filtered_word_list_4 = letter4_rules(article)
            #filtered_word_list_3 = letter3_rules(article)
            filtered_word_list_2 = letter2_rules(article)
            filtered_word_list = apply_rules_on_word(article)
            matching_stop_word = find_matching_word()
            # print('Total Word in Article File:',article_word_file)
            # print('Total Stop Word Found in Article (>3 Letters):',len(filtered_word_list_4))
            # print('Total Stop Word Found in Article (3 Letters):', len(filtered_word_list_3))
            #print('Total Stop Word Found in Article (2 Letters):', len(filtered_word_list_2))
            # print('Total Article Stop Word\'s Match with Stop Word File :', matching_stop_word)
            # print("--------------------------------------")
            #total_stop_word_found = len(filtered_word_list_4)+len(filtered_word_list_3)+len(filtered_word_list_2)
            total_stop_word_found = len(filtered_word_list+filtered_word_list_2)
            # print("------------Our Rule-------------")
            # print(filtered_word_list)
            # print(len(filtered_word_list))
            # print("------------11 Rule-------------")
            # print(filtered_word_list_2)
            # print(len(filtered_word_list_2))

            temp = []
            for x in filtered_word_list:
                    if x in matching_word:
                        if x not in temp:
                            temp.append(x)
            for x in filtered_word_list_2:
                    if x in matching_word:
                        if x not in temp:
                            temp.append(x)
            # print("--------Combine our Rule and 11 Rule--------")
            # print(temp)
            # print(len(temp))
            # print("-------------")
            # data_for_table.append([article,article_word_file,matching_stop_word,total_stop_word_found,temp])
            data_for_table.append([article, article_word_file, matching_stop_word,len(filtered_word_list+filtered_word_list_2), len(filtered_word_list_2),len(filtered_word_list)])
            all_words = []
            stop_words = []
            matching_word = []

# main('Articles', 'Stopword2')
# for i in data_for_table:
#     print(i[0],"--",i[1])

class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.title = "Accuracy Table"
        self.left = 0
        self.top = 0
        self.width = 1920
        self.height = 1080
        self.InitUI()

    def InitUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left,self.top,self.width,self.height)
        main('Testing', 'Stopword')
        self.creatingTables()

        self.show()

    def creatingTables(self):
        vbox = QVBoxLayout()

        tableWidget = QTableWidget()
        tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        tableWidget.setRowCount(102)
        tableWidget.setColumnCount(7)

        tableWidget.setItem(0, 0, QTableWidgetItem("Article Name"))
        tableWidget.setItem(0, 1,QTableWidgetItem("Total Words In Article"))
        tableWidget.setItem(0, 2, QTableWidgetItem("Words match with Stop Words"))
        tableWidget.setItem(0, 3, QTableWidgetItem("Rule based Stop Words"))
        tableWidget.setItem(0, 4, QTableWidgetItem("Accuracy"))
        #tableWidget.setItem(0, 5, QTableWidgetItem("Matched Stop Words"))
        tableWidget.setItem(0, 5, QTableWidgetItem("11 Rules Result"))
        tableWidget.setItem(0, 6, QTableWidgetItem("Our Rules Result"))

        avg_accuracy = 0
        avg_accuracy2 = 0
        avg_accuracy3 = 0
        count = 1
        for i in data_for_table:
            # if (round(i[3]/i[2]*100,2) > 70 and round(i[3]/i[2]*100,2) <= 100):
                tableWidget.setItem(count, 0, QTableWidgetItem(i[0]))
                tableWidget.setItem(count, 1, QTableWidgetItem(str(i[1])))
                tableWidget.setItem(count, 2, QTableWidgetItem(str(i[2])))
                tableWidget.setItem(count, 3, QTableWidgetItem(str(i[3])))

                try:
                    tableWidget.setItem(count, 4, QTableWidgetItem(str(round(i[3]/i[2]*100,2))+"%"))
                    avg_accuracy += round(i[3]/i[2]*100,2)
                    avg_accuracy2 += round(i[4] / i[2] * 100, 2)
                    avg_accuracy3 += round(i[5] / i[2] * 100, 2)
                except:
                    tableWidget.setItem(count, 4, QTableWidgetItem(str(round(0, 2)) + "%"))
                tableWidget.setItem(count, 5, QTableWidgetItem(str(round(i[4]/i[2]*100,2))+"%"))
                tableWidget.setItem(count, 6, QTableWidgetItem(str(round(i[5]/i[2]*100,2))+"%"))
                count += 1

        tableWidget.setItem(count, 3, QTableWidgetItem("AVG ACCURACY"))
        tableWidget.setItem(count, 4, QTableWidgetItem(str(round(avg_accuracy/(count-1),2))))
        tableWidget.setItem(count, 5, QTableWidgetItem(str(round(avg_accuracy2 / (count - 1), 2))))
        tableWidget.setItem(count, 6, QTableWidgetItem(str(round(avg_accuracy3 / (count - 1), 2))))
        vbox.addWidget(tableWidget)
        self.setLayout(vbox)



App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())






