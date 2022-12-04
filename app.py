from PyQt5 import uic,QtWidgets
from creatEvent import create_event

def funcao_digitar():
    line_text = interface.lineEdit.text()
    print(line_text)


app = QtWidgets.QApplication([])

interface = uic.loadUi("TELA_PRINCIPAL.ui")
interface.pushButton.clicked.connect(create_event) # acionamento através do botão fale

interface.show()
app.exec()