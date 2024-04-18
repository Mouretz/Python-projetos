"""""
import pygame #importando biblioteca , esta carrega imagem, som , video entre outras
pygame.init() #iniciando a biblioteca
pygame.mixer.music.load('ex20.mp3.mp3')# carregando musica
# definindo volume tambem da mas tem q pesquisar
pygame.mixer.music.play()# comecar a tocar
input() #versao 3.9 deve colocar o input
pygame.event.wait()# espera o evento terminar pra iniciar o programa
# em cima eu que fiz o basico  abaixo e da internet
"""""
from pygame import mixer

# Starting the mixer
mixer.init()

# Loading the songp
mixer.music.load(('ex20.mp3.mp3'))

# Setting the volume


# Start playing the songp
mixer.music.play()
input()
# infinite loop
while True:

    print("Press 'p' to pause, 'r' to resume")
    print("Press 'e' to exit the program")
    query = input(" ")

    if query == 'p':

        # Pausing the music
        mixer.music.pause()
    elif query == 'r':

        # Resuming the music
        mixer.music.unpause()
    elif query == 'e':

        # Stop the mixer
        mixer.music.stop()
        break


