from sys import argv, exit
from PySide6.QtWidgets import QMainWindow, QApplication
from login_ui import Ui_MainWindow


class App(QMainWindow, Ui_MainWindow):
     
    def __init__(self):
        super().__init__()
        self.setupUi(self)


if __name__ == '__main__':
    app = QApplication(argv)
    janela = App()
    janela.show()
    exit(app.exec())        
   