import webbrowser
from assistente import talk, listen
import wikipedia


def abrir_google():
    talk('Sobre o que você quer pesquisar?')
    voz = listen()
    url =  "http://google.com/search?q=" + voz
    webbrowser.get().open(url)
    talk("Aqui está o que encontrei sobre" + voz + 'no google')
    return

def abrir_youtube():
    talk('Sobre o que você quer pesquisar no youtube?')
    voz = listen()
    url = "http://www.youtube.com/results?search_query=" + voz
    webbrowser.get().open(url)
    talk("Aqui está o que encontrei sobre" + voz + 'no youtube')
    return

def wiki():
    talk('Sobre o que você quer pesquisar no wikipedia?')
    voz = listen()
    result = wikipedia.summary(voz)
    talk("Aqui está o que encontrei sobre" + voz + 'no wikipedia')
    return result
