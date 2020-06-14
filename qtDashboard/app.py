from PySide2 import QtWidgets, QtCore, QtWebEngineWidgets



# WINDOWS APP
class Windows(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.setStyleSheet("QWidget{background-color: #343a40;}")

        self.main_layout = QtWidgets.QGridLayout(self)

        self.spin = QtWidgets.QSpinBox()
        self.spin.setValue(30)
        self.spin.setRange(7, 1200)

        self.btn_refresh = QtWidgets.QPushButton("Rafraichir")
        self.btn_refresh.clicked.connect(self.refresh)

        self.spin.setStyleSheet("color: white;")
        self.btn_refresh.setStyleSheet("color: white;")
        self.btn_refresh.setFlat(True)

        self.view = QtWebEngineWidgets.QWebEngineView()
        self.view.load(QtCore.QUrl("http://claquirou.pythonanywhere.com/"))
        self.setWindowTitle("Tableau de bord- Devise")

        self.main_layout.addWidget(self.spin, 0, 0, 1, 1)
        self.main_layout.addWidget(self.btn_refresh, 0, 1, 1, 1)
        self.main_layout.addWidget(self.view, 1, 0, 1, 2)

    def refresh(self):
        days = self.spin.value()
        self.view.load(QtCore.QUrl(f"http://claquirou.pythonanywhere.com/days={days}&currencies=CAD,USD,CHF,PHP"))

app = QtWidgets.QApplication([])
win = Windows()
win.showFullScreen()
app.exec_()