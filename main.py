import sys

from PyQt5 import QtWidgets, uic
from PyQt5.QtCore import QTimer

from clock import Clock


class MainClock(QtWidgets.QMainWindow):
    """
    Classe da janela principal
        Responsável por inserir data e hora do sistema e atualizá-las
        no seu respectivo tempo
    """
    def __init__(self):
        super(MainClock, self).__init__()
        uic.loadUi("./views/main.ui", self)
        self.cls_clock = Clock()
        timer = QTimer(self)
        timer.timeout.connect(self.insert_now)
        timer.timeout.connect(self.insert_today)
        timer.start(1000)

    def insert_now(self):
        """
        Insere hora atual do sistema na GUI
        """
        now = self.cls_clock.get_now()
        self.clock_label.setText(str(now))

    def insert_today(self):
        """
        insere data atual do sistema na GUI
        """
        today = self.cls_clock.get_today()
        self.date_label.setText(str(today))


app = QtWidgets.QApplication(sys.argv)
window = MainClock()
window.show()
app.exec_()
