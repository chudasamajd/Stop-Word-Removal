from NewRules_For_Comparision_Table_For_Our_Rules import main as m1
from NewRules_For_Comparision_Table_For_11_Rules import main as m2
from NewRules_For_Comparision_Table_For_17_Rules import main as m3
import string
import os
from PyQt5.QtWidgets import QApplication, QWidget, QTableWidget, QTableWidgetItem,QVBoxLayout,QAbstractItemView
import sys
from PyQt5 import QtGui

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
        self.our_rule = m1('Big Articles','Stopword2')
        self.rule_11 = m2('Big Articles','Stopword2')
        self.rule_17 = m3('Big Articles', 'Stopword2')
        self.creatingTables()

        self.show()

    def creatingTables(self):
        vbox = QVBoxLayout()

        tableWidget = QTableWidget()
        tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        tableWidget.setRowCount(3)
        tableWidget.setColumnCount(4)

        tableWidget.setItem(0, 1, QTableWidgetItem("Base Paper Rules"))
        tableWidget.setItem(0, 2,QTableWidgetItem("Proposed Rules"))
        tableWidget.setItem(0, 3, QTableWidgetItem("All Rules"))

        tableWidget.setItem(1, 0, QTableWidgetItem("<3 Letters"))
        tableWidget.setItem(1, 1, QTableWidgetItem(str(self.rule_11)+"%"))
        tableWidget.setItem(1, 2, QTableWidgetItem("-"))
        tableWidget.setItem(1, 3, QTableWidgetItem(str(self.rule_17) + "%"))

        tableWidget.setItem(2, 0, QTableWidgetItem(">2 Letters"))
        tableWidget.setItem(2, 1, QTableWidgetItem("-"))
        tableWidget.setItem(2, 2, QTableWidgetItem(str(self.our_rule)+"%"))



        vbox.addWidget(tableWidget)
        self.setLayout(vbox)



App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())






