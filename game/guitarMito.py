import pygame
import math
from pygame import mixer

def notePress(button):
    for i in range(number_notes):
        if note_pressable[i]:
            if note_key[i] == button:
                noteImg[i] = pygame.image.load(pressedNoteColors[i % 4])
                noteY_change[i] = 0
                noteY[i] = 520
                noteX_change[i] = 0

def plotNote(x, y, i):
    screen.blit(noteImg[i], (x, y))


# Iniciando o Pygame
pygame.init()
pygame.display.set_caption('Guitar Mito')

# Musica de fundo
mixer.music.load('./Assets/Better Call Saul Intro.mp3')
mixer.music.play()

# Criando a tela
screen = pygame.display.set_mode((800, 600))
background = pygame.image.load('./Assets/background.jpg')

# Criando teclas
keysOrder = ['blue', '']
keys = ['a', 's', 'd', 'f']
xChange = [-0.05, -0.02, 0.01, 0.05]
noteColors = ['./Assets/green-button.png', './Assets/red-button.png', './Assets/blue-button.png', './Assets/yellow-button.png', './Assets/blue-button.png']
pressedNoteColors = ['./Assets/green-up.png', './Assets/red-up.png', './Assets/blue-up.png', './Assets/yellow-up.png', './Assets/blue-up.png']
noteTime = [-60, -40, 60, 10, -100]

# Criando Notas
noteImg = []
noteX = []
noteY = []
noteX0 = []
noteX_change = []
noteY_change = []
note_pressable = []
note_key = []
number_notes = 5
rows = []

cont = 0
for i in range(number_notes):
    noteImg.append(pygame.image.load(noteColors[i]))
    noteX.append(360 + cont)
    noteX0.append(360 + cont)
    noteY.append(noteTime[i])
    noteX_change.append(xChange[i % 4])
    noteY_change.append(0.15)
    note_pressable.append(False)
    note_key.append(keys[i % 4])
    cont += 30
    cont = cont % 400

running = True
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
                #noteY[i] = 230
                #noteX[i] = noteX0[i]
                note_pressable[i] = False

            plotNote(noteX[i], noteY[i], i)

    pygame.display.update()
