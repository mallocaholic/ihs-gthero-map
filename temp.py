import pygame, sys
import math
from pygame import mixer

def notePress(button):
    for i in range(number_notes):
        if note_pressable[i]:
            if note_key[i] == button:
                noteImg[i] = pygame.image.load(pressedNoteColors[keysOrder[i]])
                noteY_change[i] = 0
                noteY[i] = 520
                noteX_change[i] = 0
                plot[i] = False

def plotNote(x, y, i):
    if plot[i]:
        screen.blit(noteImg[i], (x, y))

#função para iniciar o jogo:
def initGame(running): 
    #criando as notas
    for i in range(number_notes):
        noteImg.append(pygame.image.load(noteColors[keysOrder[i]]))
        noteX.append(initialX[keysOrder[i]])
        noteX0.append(keysOrder[i])
        noteY.append(noteTime[i])
        noteX_change.append(xChange[keysOrder[i]])
        noteY_change.append(0.15)
        note_pressable.append(False)
        note_key.append(keys[keysOrder[i]])
        plot.append(True)

    vida = 100

    # Musica
    mixer.music.load('Assets/Better_Call_Saul_Intro.mp3')
    mixer.music.play()
    
    while running:
        screen.fill((0, 5, 20))

        # Imagem de fundo
        screen.blit(background, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # Teclado
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    notePress('a')
                if event.key == pygame.K_s:
                    notePress('s')
                if event.key == pygame.K_d:
                    notePress('d')
                if event.key == pygame.K_f:
                    notePress('f')
                if event.key == pygame.K_t:
                    running = menuLost(running)

        if running:
            for i in range(number_notes):
                noteY[i] += noteY_change[i]

                if noteY[i] > 230:
                    noteX[i] += noteX_change[i]
                    
                    #area apertável
                    if 480 <= noteY[i]:
                        note_pressable[i] = True

                    #nota não pode mais ser apertada (passou do limite)
                    if noteY[i] > 540:
                        note_pressable[i] = False
                        vida = vida - 10

                    plotNote(noteX[i], noteY[i], i)

        if running != False:
            pygame.display.update()

#tela de quando vc perde
def menuLost(state):
    state = 1
    while(state):
        mixer.music.pause()
        pygame.display.update()
        screen.blit(background_perdeu, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                return 0 

def mainMenu(running):
    background_menu = pygame.image.load('Assets/backbround_menu.png')
    background_menu = pygame.transform.scale(background_menu, res)

    while running:
        screen.blit(background_menu, (0, 0))
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                running = False   
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    initGame(running)


# Carregando as telas
res = (800, 600)
screen = pygame.display.set_mode(res)
background = pygame.image.load('Assets/background.jpg')
background_perdeu = pygame.image.load('Assets/background_gameover.png')

# Criando teclas
keysOrder = ['green', 'red', 'blue', 'yellow', 'red', 'blue', 'green', 'red', 'blue', 'green', 'red', 'blue', 'yellow', 'green', 'red', 
 'green', 'red', 'blue', 'yellow', 'blue', 'green', 'red', 'blue', 'yellow', 'blue', 'yellow', 'blue', 'yellow',
 'blue', 'blue', 'blue', 'blue', 'yellow', 'red', 'red', 'yellow', 'yellow', 'yellow'
]

keys = {'green': 'a', 'red': 's', 'blue': 'd', 'yellow': 'f'}
initialX = {'green': 360, 'red': 390, 'blue': 420, 'yellow': 450}
xChange = {'green': -0.05, 'red': -0.02, 'blue': 0.01, 'yellow': 0.05}
noteColors = {'green': 'Assets/green-button.png', 'red': 'Assets/red-button.png', 'blue': 'Assets/blue-button.png', 'yellow': 'Assets/yellow-button.png'}
pressedNoteColors = {'green': 'Assets/green-up.png', 'red': 'Assets/red-up.png', 'blue': 'Assets/blue-up.png', 'yellow': 'Assets/yellow-up.png'}
noteTime = [50, 50, 50, 50, 0, 0, -16, -32, -50, -100, -100, -100, -100, -116, -132, 
            -150, -150, -150, -150, -200, -216, -232, -282, -282, -332, -332, -347, -347,
            -397, -447, -497, -547, -572, -622, -672, -722, -747, -772]
            
# Criando Notas
noteImg = []
noteX = []
noteY = []
noteX0 = []
noteX_change = []
noteY_change = []
note_pressable = []
note_key = []
number_notes = len(keysOrder)
rows = []
plot = []


# Iniciando o Pygame
pygame.init()
pygame.display.set_caption('Guitar Mito')
mainMenu(True)
pygame.exit()

