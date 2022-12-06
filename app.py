from creatEvent import *
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

    interface.label_2.setText("Qual Qual a data e hora final do evento?")
    interface.label_2.adjustSize()
    end_date = take_end_date()
    interface.label_3.setText(end_date)
    interface.label_3.adjustSize()
    
    time.sleep(0.5)

    create_event(event_title, event_desc, start_date, end_date)


def comando_voz():
    try:
        talk('Olá, como posso te ajudar?')
        voz = listen()
        print(voz)
        if voz == 'criar evento':
            adm_evento_voz()
            talk('algo mais?')
        elif voz == 'pesquisar' or 'pequisa':
            abrir_google()
            talk('algo mais?')
        elif voz == 'youtube':
            abrir_youtube()
            talk('algo mais?')
        elif voz == 'wikipedia':
            wiki()
            talk('algo mais?')
        else:
            voz == 'sair'
    
    except:
        talk('não entendi, tente novamente')
        comando_voz()


interface.pushButton_2.clicked.connect(comando_voz)
interface.show()
application.exec()