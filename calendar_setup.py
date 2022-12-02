from datetime import datetime
from google1 import get_calendar_service
from assistente import *
import time

calendar_service = get_calendar_service()


def take_event_title():
    talk("Qual o titulo do evento?")
    listened_title = listen()
    return listened_title

def take_event_desc():
    talk("Qual a descrição do evento?")
    listen_desc = listen()
    return listen_desc

def take_start_date():
    talk("Qual o horário inicial?")
    listened_date = listen().replace(' as ', ' de ')
    if '2000' in listened_date:
        listened_date = listened_date.replace('2000 22', '2022')
    print(listened_date)
    listened_date = listened_date.split(' de ')
    new_date = listened_date[2] + '-' + listened_date[1] + '-' + listened_date[0]\
        + ' ' + listened_date[3]
    date_isoformat = datetime.fromisoformat(new_date).isoformat()
    return date_isoformat

def take_end_date():
    talk("Qual o horário final?")
    listened_date = listen().replace(' às ', ' de ')
    if '2000' in listened_date:
        listened_date = listened_date.replace('2000 22', '2022')
    listened_date = listened_date.split(' de ')
    new_date = listened_date[2] + '-' + listened_date[1] + '-' + listened_date[0]\
        + ' ' + listened_date[3]

    date_isoformat = datetime.fromisoformat(new_date).isoformat()
    return date_isoformat



def create_event():
    event_title = take_event_title()
    time.sleep(0.5)
    event_desc = take_event_desc()
    time.sleep(0.5)
    start_date = take_start_date()
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

    print("Evento criado com sucesso!")


if __name__ == '__main__':
    create_event()