from PyQt5 import uic,QtWidgets
from creatEvent import create_event, create_manual

def funcao_digitar():
    line_text = interface.lineEdit.text()
    print(line_text)


app = QtWidgets.QApplication([])

interface = uic.loadUi("TELA_PRINCIPAL.ui")

interface.pushButton_2.clicked.connect(create_event) # acionamento através do botão fale
interface.pushButton.clicked.connect(create_manual)#botão pra acionar por texto


interface.show()
app.exec()