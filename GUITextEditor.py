from PyQt5.QtWidgets import *
from PyQt5 import uic

class MyGUI(QMainWindow):
    def __init__(self):
        super(MyGUI, self).__init__()
        uic.loadUi('editor.ui', self)
        self.show()

        self.setWindowTitle("Notepad")
        self.action12pt.triggered.connect(lambda: self.change_size(12))
        self.action18pt.triggered.connect(lambda: self.change_size(18))
        self.action24pt.triggered.connect(lambda: self.change_size(24))

        self.actionOpen.triggered.connect(self.open_file)

    def change_size(self, size):
        self.plainTextEdit.setFont(QFont("Arial", size))

    def open_file(self):
        options = QFileDialog.Options()
        filename, _ = QFileDialog.getOpenFileName(self, "Open File", "Text Files (*.txt)::Python Files (*py)", options=options)


def main():
    app = QApplication()
    window = MyGUI()
    app.exec_()

if __name__ == '__main__':
    main()