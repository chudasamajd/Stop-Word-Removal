import sys
from random import randint
from GUI_17_Rules import extractAllWords,apply_rules_on_word
import time
import os

from PyQt5.QtWidgets import (
    QApplication,
    QLabel,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QWidget,
    QGridLayout,
    QFileDialog,
    QTextEdit
)

from PyQt5.QtCore import QDir


input_file_name = ''

def convert_bytes(num):
    """
    this function will convert bytes to MB.... GB... etc
    """
    for x in ['bytes', 'KB', 'MB', 'GB', 'TB']:
        if num < 1024.0:
            return "%3.1f %s" % (num, x)
        num /= 1024.0


def file_size(file_path):
    """
    this function will return the file size
    """
    if os.path.isfile(file_path):
        file_info = os.stat(file_path)
        return convert_bytes(file_info.st_size)



class Window1(QWidget):
    def __init__(self):
        super().__init__()

        self.resize(500, 400)

        layout = QVBoxLayout()
        grid = QGridLayout()

        self.t1 = QTextEdit()
        self.label1 = QLabel("Total Words : 00")
        #self.label2 = QLabel("Total Time : 00 Sec.")
        self.load_data()

        grid.addWidget(self.label1, 0, 0, 1, 1)
        #grid.addWidget(self.label2, 0, 1, 1, 1)
        grid.addWidget(self.t1, 1, 0, 1, 2)

        layout.addLayout(grid)

        self.setLayout(layout)

    def load_data(self):
        global input_file_name
        if input_file_name != '':
            initialTime = time.time()
            with open(input_file_name, 'r', encoding='utf8') as f:
                file_data = f.read()
                self.t1.setPlainText(file_data)
                f.close()
                time.sleep(1)
            finalTime = time.time()
            wordstring = open(input_file_name, encoding="utf-8").read()
            wordlist = wordstring.split()

            self.label1.setText("Total Size : "+str(file_size(input_file_name)))
            #self.label2.setText("Total Time : "+str(finalTime - initialTime)+" Sec.")


class Window2(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(500, 400)

        layout = QVBoxLayout()
        grid = QGridLayout()

        self.t1 = QTextEdit()
        self.label1 = QLabel("Total Words : 00")
        #self.label2 = QLabel("Total Time : 00 Sec.")
        self.load_data()

        grid.addWidget(self.label1, 0, 0, 1, 1)
        #grid.addWidget(self.label2, 0, 1, 1, 1)
        grid.addWidget(self.t1, 1, 0, 1, 2)

        layout.addLayout(grid)

        self.setLayout(layout)

    def load_data(self):
        global input_file_name
        if input_file_name != '':
            word_left = apply_rules_on_word(input_file_name)
            initialTime = time.time()
            with open('Output/result.txt', 'r', encoding='utf8') as f:
                file_data = f.read()
                self.t1.setPlainText(file_data)
                f.close()
                time.sleep(1)
            finalTime = time.time()
            self.label1.setText("Total Size : "+str(file_size('Output/result.txt')))
            #self.label2.setText("Total Time : "+str(finalTime - initialTime)+" Sec.")



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Main")
        self.resize(300, 100)



        l = QVBoxLayout()
        grid = QGridLayout()
        self.button1 = QPushButton('Select Article File')
        self.button1.clicked.connect(self.get_text_file)

        self.button2 = QPushButton('Not Remove Stopword')
        self.button2.clicked.connect(self.toggle_window1)

        self.button3 = QPushButton('Remove Stopword')
        self.button3.clicked.connect(self.toggle_window2)

        grid.addWidget(self.button1, 0, 0, 1, 2)
        grid.addWidget(self.button2, 1, 0, 1, 1)
        grid.addWidget(self.button3, 1, 1, 1, 1)

        l.addLayout(grid)


        w = QWidget()
        w.setLayout(l)
        self.setCentralWidget(w)

    def toggle_window1(self, checked):
        self.window1 = Window1()
        if self.window1.isVisible():
            self.window1.hide()

        else:
            self.window1.show()

    def toggle_window2(self, checked):
        self.window2 = Window2()
        if self.window2.isVisible():
            self.window2.hide()

        else:
            self.window2.show()

    def get_text_file(self):
        global input_file_name
        dialog = QFileDialog()
        dialog.setFileMode(QFileDialog.AnyFile)
        dialog.setFilter(QDir.Files)

        if dialog.exec_():
            file_name = dialog.selectedFiles()

            print(file_name[0])
            if file_name[0].endswith('.txt'):
                input_file_name = file_name[0]



app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec_()