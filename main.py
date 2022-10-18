import pygame
from pygame import mixer
import os, sys
from fcntl import ioctl
import time

## Setando coisas
RD_SWITCHES   = 24929
RD_PBUTTONS   = 24930
WR_L_DISPLAY  = 24931
WR_R_DISPLAY  = 24932
WR_RED_LEDS   = 24933
WR_GREEN_LEDS = 24934

# Criando teclas
keysOrder = ['green', 'red', 'blue', 'yellow', 'red', 'blue', 'green', 'red', 'blue', 'green', 'red', 'blue', 'yellow', 'green', 'red', 
 'green', 'red', 'blue', 'yellow', 'blue', 'green', 'red', 'blue', 'yellow', 'blue', 'yellow', 'blue', 'yellow',
 'blue', 'blue', 'blue', 'blue', 'yellow', 'red', 'red', 'yellow', 'yellow', 'yellow'
]

keys = {'green': 'a', 'red': 's', 'blue': 'd', 'yellow': 'f'}
initialX = {'green': 360, 'red': 390, 'blue': 420, 'yellow': 450}
xChange = {'green': -4.0, 'red': -1.6, 'blue': 0.8, 'yellow': 4.0}
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

mapping = {'0': '40', '1': '79', '2': '24', '3': '30', '4': '19', '5': '12', '6': '02', '7': '78', '8': '00', '9': '10', 'F': 'FF'}

def piscarHit(a):
    currentTime = time.time()

    state = ""

    if currentTime - a[1] < 0.2:
        state = "11111111" # Liga
    else:
        state = "00000000" # Desliga 
        a = (0,.0)

    
    data = int(state, 2)
    ioctl(fd, WR_GREEN_LEDS)
    retval = os.write(fd, data.to_bytes(4, 'little'))

    return a

def updateScore(val):

    val_str = str(val)
    str_emp = ""

    for number in val_str:
        str_emp += mapping[number] 

    while(len(str_emp) < 8):
        str_emp = mapping['0'] + str_emp

    data = int(str_emp, 16)
    ioctl(fd, WR_R_DISPLAY)
    retval = os.write(fd, data.to_bytes(4, 'little'))
    #print("wrote %d bytes"%retval)
    

def piscar(score):
    time.sleep(0.2)
    updateScore('FFFF')
    updateScore('FFFF')
    time.sleep(0.2)
    updateScore(score)
    time.sleep(0.2)
    updateScore(score)

def toArray(red):
    a = []
    for i in range(4):
        res = red & (1 << i)
        if res:
            a.append(0)         #0 nao foi pressionado
        else:
            a.append(1)         #1 foi pressionado
    return a

def notePress(button):
    ret_val = 0
    for i in range(number_notes):
        if note_pressable[i]:
            if note_key[i] == button:
                noteImg[i] = pygame.image.load(pressedNoteColors[keysOrder[i]])
                noteY_change[i] = 0
                noteY[i] = 520
                noteX_change[i] = 0
                plot[i] = False
                ret_val = 1
                note_pressable[i] = False

    return ret_val

def plotNote(x, y, i):
    if plot[i]:
        screen.blit(noteImg[i], (x, y))

#função para iniciar o jogo:
def initGame(): 
    initialTime = time.time()
    print(initialTime)
    running = 1
    score = 0
    updateScore(score)
    #criando as notas
    for i in range(number_notes):
        noteImg.append(pygame.image.load(noteColors[keysOrder[i]]))
        noteX.append(initialX[keysOrder[i]])
        noteX0.append(keysOrder[i])
        noteY.append(noteTime[i])
        noteX_change.append(xChange[keysOrder[i]])
        noteY_change.append(12)
        note_pressable.append(False)
        note_key.append(keys[keysOrder[i]])
        plot.append(True)

    #carregando a tela de jogo
    background = pygame.image.load('Assets/background.jpg')

    vida = 75

    # Musica
    mixer.music.load('Assets/Better_Call_Saul_Intro.mp3')
    #mixer.music.play()
    flagMusic = 0

    # Note hits
    nHit = (0,.0)
    
    while 1:
        screen.fill((0, 5, 20))

        currentTime = time.time()
        if (currentTime - initialTime > 5) and not flagMusic:
            mixer.music.play()
            flagMusic = 1


        # Imagem de fundo
        screen.blit(background, (0, 0))

        ioctl(fd, RD_PBUTTONS)
        red = os.read(fd, 4); # read 4 bytes and store in red var
        red = int.from_bytes(red, 'little')
        pressedButtons = toArray(red)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = 0

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    notePress('a')
                if event.key == pygame.K_s:
                    notePress('s')
                if event.key == pygame.K_d:
                    notePress('d')
                if event.key == pygame.K_f:
                    notePress('f')
                if event.key == pygame.K_p:
                    #indo para a tela 'perdeu'
                    return (2,1, score)
                if event.key == pygame.K_g:
                    #indo para a tela 'perdeu'
                    return (3,1, score)


        # Periféricos 
        if(pressedButtons[0]):
            if notePress('f'):
                score = score + 8
                updateScore(score)
                nHit = (1,currentTime)
        if(pressedButtons[1]):
            if notePress('d'):
                score = score + 8
                updateScore(score)
                nHit = (1,currentTime)
        if(pressedButtons[2]):
            if notePress('s'):
                score = score + 9
                updateScore(score)
                nHit = (1,currentTime)
        if(pressedButtons[3]):
            if notePress('a'):
                score = score + 11
                updateScore(score)
                nHit = (1,currentTime)
        
        # print(score)
        updateScore(score)
        updateScore(score)

        #see if note was hit


        nHit = piscarHit(nHit)



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
                        #ajietar vida!!!!
                        vida = vida - 1

                    plotNote(noteX[i], noteY[i], i)

               # if mixer.music.get_busy() == False:
                if i == number_notes - 1 and noteY[i] > 480:
                    initialTime = time.time()
                    print(initialTime)
                    return (3, 1, score)

        if running != 0:
            time.sleep(0.15)
            pygame.display.update()

        if vida <= 0:
            return (2, 1, score)


#tela de quando vc perde
def menuLost():

    #carregando a tela 'perdeu'
    background_perdeu = pygame.image.load('Assets/background_gameover.png')

    while 1:
        mixer.music.pause()
        pygame.display.update()
        screen.blit(background_perdeu, (0, 0))

        piscarHit((0,0))
        time.sleep(0.5)
        ioctl(fd, RD_PBUTTONS)
        red = os.read(fd, 4); # read 4 bytes and store in red var
        red = int.from_bytes(red, 'little')
        pressedButtons = toArray(red)

        if pressedButtons[0] or pressedButtons[1] or pressedButtons[2] or pressedButtons[3]:
            return (0,0)

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return (0,0) 

def mainMenu():
    background_menu = pygame.image.load('Assets/backbround_menu.png')
    background_menu = pygame.transform.scale(background_menu, res)

    while 1:
        screen.blit(background_menu, (0, 0))
        pygame.display.update()

        ioctl(fd, RD_PBUTTONS)
        red = os.read(fd, 4); # read 4 bytes and store in red var
        red = int.from_bytes(red, 'little')
        pressedButtons = toArray(red)

        if pressedButtons[0] or pressedButtons[1] or pressedButtons[2] or pressedButtons[3]:
            return (1,1)

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return (1,1)
                if event.key == pygame.K_ESCAPE:
                    return (0,0)

def menuWin(score):
    background_win = pygame.image.load('Assets/backbround_yourock.png')
    mixer.music.unload()
    urnaSound = mixer.music.load('Assets/confirma-urna.mp3')
    mixer.music.play()

    while 1:
        screen.blit(background_win, (0, 0))
        pygame.display.update()
        piscar(score)

        ioctl(fd, RD_PBUTTONS)
        red = os.read(fd, 4); # read 4 bytes and store in red var
        red = int.from_bytes(red, 'little')
        pressedButtons = toArray(red)

        if pressedButtons[0] or pressedButtons[1] or pressedButtons[2] or pressedButtons[3]:
            return (0,0)

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return (0,0)



# Main
if __name__ == '__main__':
    state = 0
    score = 0

    if len(sys.argv) < 2:
        print("Error: expected more command line arguments")
        print("Syntax: %s </dev/device_file>"%sys.argv[0])
        exit(1)

    fd = os.open(sys.argv[1], os.O_RDWR)
    updateScore(0)


    #carregando a tela
    res = (800, 600)
    screen = pygame.display.set_mode(res)

    # running = [0 - para de rodar o jogo, 1 - jogo rodando, 2 - tela de perdeu]
    running = 1
    pygame.init()
    
    while running:
        if state == 0:
            state, running = mainMenu()
        elif state == 1:
            state, running, score = initGame()
        elif state == 2:
            state, running = menuLost()
        elif state == 3:
            state, running = menuWin(score)

    mixer.music.unload()
    os.close(fd)
    pygame.quit()
