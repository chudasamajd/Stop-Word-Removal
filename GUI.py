import sys
from PyQt5.QtWidgets import (QMainWindow,QGridLayout,QApplication,QWidget,QFileDialog,QTextEdit,QPushButton,QLabel,QVBoxLayout)
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QDir


class DialogApp(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(800,600)


        self.button1 = QPushButton('Select Article File')
        self.button1.clicked.connect(self.get_text_file)
        self.button2 = QPushButton('Normal Analysis')
        self.button3 = QPushButton('Apply Rules')
        self.t1 = QTextEdit()

        layout = QVBoxLayout()

        grid =  QGridLayout()
        l1 = QLabel("Demo")
        # addWidget(self.t1, row, column, row span, col span)
        grid.addWidget(self.button1, 0, 0, 1, 2)
        grid.addWidget(self.button2, 1, 0, 1, 1)
        grid.addWidget(self.button3, 1, 1, 1, 1)
        grid.addWidget(self.t1, 2, 0, 1, 2)

        layout.addLayout(grid)

        # layout.addWidget(self.button1)
        # layout.addWidget(self.button2)
        # layout.addWidget(self.t1)

        self.setLayout(layout)

    def get_text_file(self):
        dialog = QFileDialog()
        dialog.setFileMode(QFileDialog.AnyFile)
        dialog.setFilter(QDir.Files)

        if dialog.exec_():
            file_name = dialog.selectedFiles()
            print(file_name[0])
            if file_name[0].endswith('.txt'):
                with open(file_name[0],'r',encoding='utf8') as f:
                    data = f.read()
                    self.t1.setPlainText(data)
                    f.close()
            else:
                pass



if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = DialogApp()
    demo.show()

    sys.exit(app.exec_())






