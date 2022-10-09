import pygame
import math
import random


def isColision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt((math.pow((enemyX - bulletX), 2)) + (math.pow((enemyY - bulletY), 2)))
    if distance < 27:
        return True
    else:
        return False

def notePress(button):
    for i in range(number_notes):
        if note_pressable[i]:
            if note_key[i] == button:
                noteY[i] = 0

def plotNote(x, y, i):
    screen.blit(noteImg[i], (x, y))


# Iniciando o Pygame
pygame.init()
pygame.display.set_caption('Guitar Mito')

# Criando a tela
screen = pygame.display.set_mode((800, 600))
background = pygame.image.load('./Assets/background.jpg')

# Criando teclas
keys = ['a', 's', 'd', 'f']
xChange = [-0.02, -0.01, 0.01, 0.02]

# Criando Notas
noteImg = []
noteX = []
noteY = []
noteX_change = []
noteY_change = []
note_pressable = []
note_key = []
number_notes = 4
rows = []

cont = 0
for i in range(number_notes):
    noteImg.append(pygame.image.load('./Assets/blue-button.png'))
    noteX.append(230 + cont)
    noteY.append(50)
    noteX_change.append(xChange[i % 4])
    noteY_change.append(0.2)
    note_pressable.append(False)
    note_key.append(keys[i % 4])
    cont += 100
    cont = cont % 400

running = True
while running:
    screen.fill((0, 5, 20))

    # Imagem de fundo
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    for i in range(number_notes):
        noteY[i] += noteY_change[i]
        noteX[i] += noteX_change[i]

        if 480 <= noteY[i] <= 520:
            note_pressable[i] = True

        if noteY[i] > 520:
            noteY[i] = 0

        plotNote(noteX[i], noteY[i], i)

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

    pygame.display.update()
