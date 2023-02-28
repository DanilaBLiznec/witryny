#pobranie biblioteki pygame
import pygame

#utworzenie funkcji waz
def waz():
    #inicjializacja biblioteki
    pygame.init()
    #utworzenie okna gry i okreslenie jego rozmiarow
    oknoGry=pygame.display.set_mode((600,600),0,32)
    #ustawiamy nazwe okna
    pygame.display.set_caption("Gra Wąż")
    #tworzymy zmienną ktora przechowuje informacje czy gra jest uruchomiona 
    run=True
    #petla while sprawdza czy warunek w zmiennej run jest prawdziwy, jak jest nieprawdziwy konczy swoje dzialanie
    while(run):
        #wypelnenie okna kolorem
        oknoGry.fill((0,0,0))
        #ustawienie opoznenie odswiezania gry
        pygame.time.delay(200)
        #sprawdzanie czy istnije jakis zdradzenie i zapisanie ich do zmiennej zdradzenie
        for zdarzenia in pygame.event.get():
            #jezeli zmienna zdradzenie przechowywuje nacisneinie przyciskyu zamknij to zmieniamy wartosc zmiennej "run"
            if zdarzenia.type==pygame.QUIT:
                run=False
            #rysowanie weza
            #definiujemy ksztalt weza
            ksztaltWaz=pygame.Rect((300,300),(15,15))
            #dodanie ksztaltu do okienka
            pygame.draw.rect(oknoGry,(255,0,0),ksztaltWaz)

        pygame.display.update()
#wywplanie funkcji pozwala na uruchomienie gry
waz()
