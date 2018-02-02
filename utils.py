import random
import pygame as pg
from initializers import *
from classes import *

'''
un nuevo estado simplemente significa la posición cambiada 
del rectángulo y el círculo. el rectángulo se movería según 
la acción óptima, el círculo cae libremente.
'''
def new_state_after_action(s, act):
    rct = None

    if act == 2:  # 0 == stay, 1 == left, 2 == right
        if s.rect.right + s.rect.width > windowWidth:
            rct = s.rect
        else:
            rct = pg.Rect(s.rect.left + s.rect.width, s.rect.top, s.rect.width,
                          s.rect.height)  # Rect(left, top, width, height)
    elif act == 1:  # action is left
        if s.rect.left - s.rect.width < 0:
            rct = s.rect
        else:
            rct = pg.Rect(s.rect.left - s.rect.width, s.rect.top, s.rect.width,
                          s.rect.height)  # Rect(left, top, width, height)

    else:  # action is 0, means stay where it is
        rct = s.rect

    newCircle = Circle(s.circle.circleX, s.circle.circleY + crclYStepFalling)

    return State(rct, newCircle)

'''
casi similar a un nuevo estado, separándose por cierta facilidad
'''
def new_rect_after_action(rect, act):
    if act == 2:  # 0 == left, 1 == right
        if rect.right + rect.width > windowWidth:
            return rect
        else:
            return pg.Rect(rect.left + rect.width, rect.top, rect.width,
                           rect.height)  # Rect(left, top, width, height)
    elif act == 1:  # action is left
        if rect.left - rect.width < 0:
            return rect
        else:
            return pg.Rect(rect.left - rect.width, rect.top, rect.width,
                           rect.height)  # Rect(left, top, width, height)
    else:  # action if to stay
        return rect

'''
define dónde debe estar la posición x inicial del círculo al caer.
'''
def circle_falling(crclradius):
    multiplier = (random.randint(0, 8)*100)+50  # make more channel by making it a floating point number
    return multiplier

'''
calcule el puntaje basado en la posición relativa del círculo y el rectángulo.
'''
def calculate_score(rect, circle):
    #print ('RL: ' + str(rect.left) + ' RL: ' + str(rect.right) +  ' CX: ' + str(circle.circleX))
    if (rect.left == 200) or (rect.left == 300) or (rect.left == 400) or (rect.left == 500) or (rect.left == 600):
        if rect.left <= circle.circleX <= rect.right:  # if the circle'x x position is between the rectangles left and right
            #print('Caught!')
            return 2
        elif circle.circleX<200 or circle.circleX>700:
            #print('No moved!')
            return 1
        else:
            #print('Gool!')
            return -2
    else:
        if circle.circleX < 200 or circle.circleX > 700:
            #print('Moved!')
            return -1
        else:
            #print('Gool!')
            return -2






    if (circle.circleX == 50) or (circle.circleX == 100) or (circle.circleX == 150) or (circle.circleX == 200) or (circle.circleX == 250):
        if rect.left <= circle.circleX <= rect.right:  # if the circle'x x position is between the rectangles left and right
            return 2
        else:
            return -2
    else:
        if (rect.left == 200) or (rect.left == 300) or (rect.left == 400) or (rect.left == 500) or (rect.left == 600):
            return +1
        else:
            return -1

'''
numpy array no puede funcionar con objetos personalizados como índices.
es por eso que debemos crear una representación entera de los estados 
donde la posición del rectángulo y el círculo combinados deberían darnos 
un identificador único. estamos almacenando el valor en otro diccionario 
que contendría los índices únicos.
'''


def state_to_number(s):
    r = s.rect.left
    c = s.circle.circleY

    if isinstance(c, float):
        a,b=str(c).split('.')
        c = str(a)
    n = int(str(r) + str(c) + str(s.circle.circleX))

    if n in QIDic:
        return QIDic[n]
    else:
        if len(QIDic):
            maximum = max(QIDic, key=QIDic.get)  # Simplemente use 'min' en lugar de 'max' para mínimo.
            QIDic[n] = QIDic[maximum] + 1
        else:
            QIDic[n] = 1
    return QIDic[n]


def get_best_action(s):
    return np.argmax(Q[state_to_number(s), :])
