import sys
from PySide6.QtWidgets import QApplication, QPushButton

class App:
    def __init__(self) -> None:
        self.app = QApplication(sys.argv)
        self.btn = QPushButton('Texto do botão')
        self.btn.setStyleSheet('font-size: 40px; color: red')
        self.btn.show()

    def executar(self):
        self.app.exec()

if __name__ == '__main__':

    App().executar()