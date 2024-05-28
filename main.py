
from PyQt6.QtWidgets import QApplication
from aritmatikaa import Aritmatika # import dari class Aritmatika dari file aritmatikaa.py

if __name__ == '__main__':
    app = QApplication([])
    window = Aritmatika()
    window.show()
    app.exec()