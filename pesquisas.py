import webbrowser
from assistente import talk, listen
import wikipedia


def abrir_google(texto):
    url =  "http://google.com/search?q=" + texto
    webbrowser.get().open(url)
    talk("Aqui está o que encontrei sobre" + texto + 'no google')
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
    wikipedia.set_lang("pt")
    texto = wikipedia.summary(voz)
    talk("Aqui está o que encontrei sobre" + voz + 'no wikipedia')
    return texto
