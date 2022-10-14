import pygame
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


# Iniciando o Pygame
pygame.init()
pygame.display.set_caption('Guitar Mito')

# Musica de fundo
mixer.music.load('./Assets/Better Call Saul Intro.mp3')

# Criando a tela
screen = pygame.display.set_mode((800, 600))
background = pygame.image.load('./Assets/background.jpg')

# Criando teclas
keysOrder = ['blue', 'yellow', 'red', 'green', 'blue', 'yellow', 'yellow', 'blue', 'red', 'green', 'yellow', 'red', 'blue', 'green', 'green', 'yellow', 'blue', 'red', 'green']
keys = {'green': 'a', 'red': 's', 'blue': 'd', 'yellow': 'f'}
initialX = {'green': 360, 'red': 390, 'blue': 420, 'yellow': 450}
xChange = {'green': -0.05, 'red': -0.02, 'blue': 0.01, 'yellow': 0.05}
noteColors = {'green': './Assets/green-button.png', 'red': './Assets/red-button.png', 'blue': './Assets/blue-button.png', 'yellow': './Assets/yellow-button.png'}
pressedNoteColors = {'green': './Assets/green-up.png', 'red': './Assets/red-up.png', 'blue': './Assets/blue-up.png', 'yellow': './Assets/yellow-up.png'}
noteTime = [70, 20, -30, -60, -140, -530, -580, -620, -700, -900, -960, -970, -1000, -1030, -1100, -1150, -1200, -1250, -1270]

# Criando Notas
noteImg = []
noteX = []
noteY = []
noteX0 = []
noteX_change = []
noteY_change = []
note_pressable = []
note_key = []
number_notes = 19
rows = []
plot = []

cont = 0
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

running = True
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

    for i in range(number_notes):
        noteY[i] += noteY_change[i]

        if noteY[i] > 230:
            noteX[i] += noteX_change[i]

            if 480 <= noteY[i]:
                note_pressable[i] = True

            if noteY[i] > 540:
                note_pressable[i] = False

            plotNote(noteX[i], noteY[i], i)

    pygame.display.update()
