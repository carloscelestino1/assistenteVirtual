from PyQt5 import uic, QtWidgets
from creatEvent import *
from createEventManual import *
import time
from assistente import *
from pesquisas import abrir_google, abrir_youtube, wiki


application = QtWidgets.QApplication([])



def criar_evento():
    interface.label_2.setText("Qual o titulo do evento?")
    interface.label_2.adjustSize()
    event_title = take_event_title()
    interface.label_3.setText(event_title)
    interface.label_3.adjustSize()
    
    time.sleep(0.5)

    interface.label_2.setText("Qual a descrição do evento?")
    interface.label_2.adjustSize()
    event_desc = take_event_desc()
    interface.label_3.setText(event_desc)
    interface.label_3.adjustSize()
    
    time.sleep(0.5)

    interface.label_2.setText("Qual a data e hora inicial do evento?")
    interface.label_2.adjustSize()
    start_date = take_start_date()
    interface.label_3.setText(start_date)
    interface.label_3.adjustSize()
    
    time.sleep(0.5)

    interface.label_2.setText("Qual a data e hora final do evento?")
    interface.label_2.adjustSize()
    end_date = take_end_date()
    interface.label_3.setText(end_date)
    interface.label_3.adjustSize()
    
    time.sleep(0.5)

    create_event(event_title, event_desc, start_date, end_date)


def ler_assistent():
    texto = interface.label_2.text() 
    talk(texto)


def falar():
    try:
        texto = listen()
    except:
        talk('não entendi, poderia repetir?')
        falar()
    interface.lineEdit.setText(texto)


def inicio():
    interface.frameInicio.show()
    interface.label_2.setText('Olá! \nEscolha uma opção: \n1)criar evento \n2)pesquisar \n3)youtube \n4)wikipedia \n5) sair')
    interface.label_2.adjustSize()

def ler_entrada_inicio():
    interface.frameInicio.show()
    texto = interface.lineEdit.text()
    interface.lineEdit.setText("")
    interface.lineEdit_2.setText(texto)
    if (texto in {'criar evento', '1'}):
        interface.frameCriarEvento.show()
    #elif (texto in {'pesquisar', 'pequisa', '2'}):
        #interface.frameInicio.close()
        #interface.frameGoogle.show()
    elif (texto in {'youtube', '3'}):
        abrir_youtube()
    elif (texto in {'wikipedia','wikipédia', '4'}):
        texto = wiki()
        print(texto)
        interface.label_2.setText(texto)
        interface.label_2.adjustSize()
    else:
        if texto == 'sair':
            talk('ok, até mais')




#display assistente = label_2
#botão para ouvir = pushButton_3

#display cliente = label_3
#botão para falar = pushButton_2

interface = uic.loadUi("TELA_PRINCIPAL.ui")
"""#assistente fala
interface.pushButton_3.clicked.connect(ler_assistent)

#inicio
interface.pushButton_4.clicked.connect(inicio)
interface.pushButton_2.clicked.connect(falar)
interface.pushButton.clicked.connect(ler_entrada_inicio)

def frameCriarEvento():
    texto = interface.lineEdit_3.text()
    texto = list(texto)
    print(texto)
    ler_entrada_inicio()

#frame Criar evento
interface.pushButton_7.clicked.connect(inicio)
interface.pushButton_6.clicked.connect(falar)
interface.pushButton_5.clicked.connect(frameCriarEvento)

def frameGooglee():
    texto = interface.lineEdit_5.text()
    print(texto)
    abrir_google(texto)

#frame google
interface.pushButton_10.clicked.connect(inicio)
interface.pushButton_9.clicked.connect(falar)
interface.pushButton_8.clicked.connect(frameGooglee)


"""




interface.show()
application.exec()


