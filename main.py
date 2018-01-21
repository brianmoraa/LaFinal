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

    # at this position, the rectangle should be here. else loses
    if crclCentreY >= windowHeight - rctHeight - crclRadius:  # check if the rectangle is under the circle or not
        reward = calculate_score(rct, Circle(crclCentreX, crclCentreY))  # +1 or -1
        crclCentreX = circle_falling(crclRadius)  #
        crclCentreY = 100
    else:
        reward = 0  # no reward if the ball wasn't missed
        crclCentreY += crclYStepFalling  # let the circle fall freely

    s = State(rct, Circle(crclCentreX, crclCentreY))
    act = get_best_action(s)  # get the best action so far in this state
    r0 = calculate_score(s.rect, s.circle)  # get the immediate reward of this step
    s1 = new_state_after_action(s, act)  # new state after taking the best action
    # build the Q table, indexed by (state, action) pair
    Q[state_to_number(s), act] += lr * (r0 + y * np.max(Q[state_to_number(s1), :]) - Q[state_to_number(s), act])

    rct = new_rect_after_action(s.rect, act)  # new position of the rectangle
    crclCentreX = s.circle.circleX  # put the ball where it originally was before the experiment
    crclCentreY = s.circle.circleY

    window.blit(balon, ((int(crclCentreX)-50, int(crclCentreY)-50)))
    window.blit(arquero, (int(s.rect.left), 660))
    window.blit(arco, ((int(200), int(660))))
    window.blit(balon, ((int(crclCentreX) - 50, int(crclCentreY) - 50)))

    if reward == 2:  # got it!
        score += reward  # add the reward to the total score
    elif reward == -2:  # missed
        missed += reward  # add the reward to the missed count
    elif reward == 1:  # add
        score += reward  # add the reward to the missed count
    elif reward == -1:  # missed
        missed += reward  # add the reward to the missed count

    #pg.draw.rect(window, BLACK, (20, 10, 700, 40))
    text = font.render('Ganados: ' + str(score) + '  |  Perdidos: ' + str(missed) + '  |  Total: ' + str(score+missed) + '  |  iteraciones: ' + str(iterations), True, WHITE)  # update the score on the screen
    window.blit(text, (40, 20))  # render score
    iterations+=1

    pg.display.update()  # update display
    fpsClock.tick(FPS)
    if i == 10000:  # stopping condition
        break
    else:
        i += 1
