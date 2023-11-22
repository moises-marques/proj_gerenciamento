from sys import argv, exit
from PySide6.QtWidgets import QMainWindow, QApplication
from login_ui import Ui_MainWindow


class App(QMainWindow, Ui_MainWindow):
     
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.btn_pg_cadastro.clicked.connect(self.vi_tela_cad)
        self.btn_home.clicked.connect(self.vi_tela_home)
        
    def vi_tela_cad(self):
        self.pages.setCurrentIndex(2)
        
    
    def vi_tela_home(self):
        self.pages.setCurrentIndex(1)
    
    
        


if __name__ == '__main__':
    app = QApplication(argv)
    janela = App()
    janela.show()
    exit(app.exec())        
   