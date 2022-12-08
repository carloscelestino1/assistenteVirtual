from PyQt5 import uic,QtWidgets
from creatEvent import *
from createEventManual import *
import time
from assistente import *
from pesquisas import abrir_google, abrir_youtube, wiki


application = QtWidgets.QApplication([])
interface = uic.loadUi("TELA_PRINCIPAL.ui")


def adm_evento_voz():
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


def ler():
    texto = interface.label_2.text() 
    talk(texto)



def menu():
    talk('Olá, escolha uma opção')
    while True:
        interface.label_2.setText('escolha uma opção: \n1)criar evento \n2)pesquisar \n3)youtube \n4)wikipedia')
        interface.label_2.adjustSize()
        try:
            voz = listen()
            if (voz == 'criar evento'):
                adm_evento_voz()
            elif (voz in {'pesquisar', 'pequisa'}):
                abrir_google()
            elif (voz == 'youtube'):
                abrir_youtube()
            elif (voz in {'wikipedia','wikipédia'}):
                texto = wiki()
                print(texto)
                interface.label_2.setText(texto)
                interface.label_2.adjustSize()
            else:
                if voz == 'sair':
                    talk('ok, até mais')
                    break
        except:
            talk('não entendi, tente novamente')
            menu()

interface.pushButton_3.clicked.connect(ler)
interface.pushButton_2.clicked.connect(menu)

interface.show()
application.exec()