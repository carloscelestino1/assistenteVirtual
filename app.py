from creatEvent import create_event, create_manual, interface, application

def frame1():
    interface.frame_2.close()
    interface.pushButton_3.clicked.connect(create_event)

def frame2():
    interface.frame_2.show()
    linha1 = interface.lineEdit_3.text()
    linha2 = interface.lineEdit_2.text()
    linha3 = interface.dateTimeEdit.text()
    linha4 = interface.dateTimeEdit_2.text()

    return linha1, linha2, linha3, linha4

def mostrar():
    create_manual(frame2()[0], frame2()[1], frame2()[2], frame2()[3])

interface.pushButton_2.clicked.connect(frame1) # acionamento através do botão fale
interface.pushButton.clicked.connect(frame2)#botão pra acionar por texto
interface.pushButton_4.clicked.connect(mostrar)

interface.show()
application.exec()