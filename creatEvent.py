from datetime import datetime, date
from google1 import get_calendar_service
from assistente import *
import time
from PyQt5 import uic,QtWidgets

application = QtWidgets.QApplication([])
interface = uic.loadUi("TELA_PRINCIPAL.ui")
calendar_service = get_calendar_service()


def take_event_title():
    try:
        interface.label_2.setText("Qual o titulo do evento?")
        talk("Qual o titulo do evento?")
        listened_title = listen()
    except:
        talk('não entendi, tente novamente')
        listened_title = take_event_title()
    return listened_title

def take_event_desc():
    try:
        interface.label_7.setText("Qual a descrição do evento?")
        talk("Qual a descrição do evento?")
        listen_desc = listen()
    except:
        talk('não entendi, tente novamente')
        listen_desc = take_event_title()
    return listen_desc

def take_start_date():
    try:
        talk("Qual a data e horário inicial?")
        listened_date = listen().replace(' as ', ' de ')
        if '2000' in listened_date:
            listened_date = listened_date.replace('2000 22', '2022')
        listened_date = listened_date.split(' de ')
        new_date = listened_date[2] + '-' + listened_date[1] + '-' + listened_date[0]\
            + ' ' + listened_date[3]
        date_isoformat = datetime.fromisoformat(new_date).isoformat()
    except:
        talk('não entendi, tente novamente')
        date_isoformat = take_start_date()
    return date_isoformat

def take_end_date():
    try: 
        talk("Qual a data e horário final?")
        listened_date = listen().replace(' às ', ' de ')
        if '2000' in listened_date:
            listened_date = listened_date.replace('2000 22', '2022')
        listened_date = listened_date.split(' de ')
        new_date = listened_date[2] + '-' + listened_date[1] + '-' + listened_date[0]\
            + ' ' + listened_date[3]

        date_isoformat = datetime.fromisoformat(new_date).isoformat()
    except:
        talk('não entendi, tente novamente')
        date_isoformat = take_end_date()
    return date_isoformat


def create_event():
    event_title = take_event_title()
    time.sleep(0.5)
    event_desc = take_event_desc()
    time.sleep(0.5)
    start_date = take_start_date()
    print(start_date)
    time.sleep(0.5)
    end_date = take_end_date()
    time.sleep(0.5)
    event_result = calendar_service.events().insert(calendarId='primary',
        body={
            "summary": event_title,
            "description": event_desc,
            "start": {"dateTime": start_date, "timeZone": 'America/Sao_Paulo'},
            "end": {"dateTime": end_date, "timeZone": 'America/Sao_Paulo'},
        }
    ).execute()

    talk("Seu evento foi criado com sucesso!")


def create_manual(linha1, linha2, linha3, linha4):

    event_result = calendar_service.events().insert(calendarId='primary',
        body={
            "summary": linha1,
            "description": linha2,
            "start": {"dateTime": convertDatetime(linha3), "timeZone": 'America/Sao_Paulo'},
            "end": {"dateTime": convertDatetime(linha4), "timeZone": 'America/Sao_Paulo'},
        }
    ).execute()


def convertDatetime(data):
    
    data = data.split(' ')
    data2 = data[0].split('/')
    new_date = data2[2] + '-' + data2[1] + '-' + data2[0]\
            + ' ' + data[1]
    date_isoformat = datetime.fromisoformat(new_date).isoformat()
    return date_isoformat

