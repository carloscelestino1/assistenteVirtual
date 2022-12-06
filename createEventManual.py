from datetime import datetime
from google1 import get_calendar_service
from assistente import *
calendar_service = get_calendar_service()


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