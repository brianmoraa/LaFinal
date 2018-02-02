#Author: Brian Mora
import sys
from initializers import *
from pygame.locals import *
from utils import *
import pygame as pg

FPS = 20  # frames per second setting
fpsClock = pg.time.Clock()

pg.init()  # pygame initialization
window = pg.display.set_mode((windowWidth, windowHeight))  # width, height
pg.display.set_caption('Catch the ball!')

balon =  pg.image.load("images/balon.png")
campo =  pg.image.load("images/campo.jpg")
arco =  pg.image.load("images/arco.png")
arquero =  pg.image.load("images/arquero.png")

rct = pg.Rect(rctLeft, rctTop, rctWidth, rctHeight)  # Rect(left, top, width, height)

action = 1  # 0 means stay, 1 means left, 2 means right

score = 0
missed = 0
reward = 0
font = pg.font.Font(None, 30)

# set learning rate
lr = .85
y = .99

i = 0
iterations = 0

while True:
    for event in pg.event.get():
        if event.type == QUIT:  # for the quitting button on the window
            pg.quit()
            sys.exit()

    #window.fill(WHITE)  # window background
    window.blit(campo, (0, 0))

    # en esta posición, el rectángulo debería estar aquí. otro pierde
    if crclCentreY >= windowHeight - rctHeight - crclRadius:  # comprueba si el rectángulo está debajo del círculo o no
        reward = calculate_score(rct, Circle(crclCentreX, crclCentreY))#1,-1,2,-2
        crclCentreX = circle_falling(crclRadius)
        crclCentreY = 100
    else:
        reward = 0  # sin recompensa si la pelota no se perdió
        crclCentreY += crclYStepFalling  # deja que el círculo caiga libremente

    s = State(rct, Circle(crclCentreX, crclCentreY))
    act = get_best_action(s)  # obtener la mejor acción hasta ahora en este estado
    r0 = calculate_score(s.rect, s.circle)  # obtener la recompensa inmediata de este paso
    s1 = new_state_after_action(s, act)  # nuevo estado después de tomar la mejor acción
    # construir la tabla Q, indexada por par (estado, acción)
    Q[state_to_number(s), act] += lr * (r0 + y * np.max(Q[state_to_number(s1), :]) - Q[state_to_number(s), act])

    #manejo de objetos en interfaces
    rct = new_rect_after_action(s.rect, act)  #posición nueva del rectángulo
    crclCentreX = s.circle.circleX  # poner la bola donde estaba originalmente antes del experimento
    crclCentreY = s.circle.circleY
    window.blit(balon, ((int(crclCentreX)-50, int(crclCentreY)-50)))
    window.blit(arquero, (int(s.rect.left), 660))
    window.blit(arco, ((int(200), int(660))))
    window.blit(balon, ((int(crclCentreX) - 50, int(crclCentreY) - 50)))

    if reward == 2:
        score += reward
    elif reward == -2:
        missed += reward
    elif reward == 1:
        score += rewar      d
    elif reward == -1:
        missed += reward

    text = font.render('Ganados: ' + str(score) + '  |  Perdidos: ' + str(missed) + '  |  Total: ' + str(score+missed) + '  |  iteraciones: ' + str(iterations), True, WHITE)  # update the score on the screen
    window.blit(text, (40, 20))
    iterations+=1

    pg.display.update()  # actualización de la pantalla
    fpsClock.tick(FPS)

    if i == 10000:  # se detiene el programa
        break
    else:
        i += 1