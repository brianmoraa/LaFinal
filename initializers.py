import numpy as np

windowWidth = 900
windowHeight = 800

# setup colors
RED = (255, 0, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# specify circle properties
crclCentreX = 50
crclCentreY = 100
crclRadius = 50

crclYStepFalling = windowHeight / 2 # velocidad +lento -rapido

# specify rectangle properties
rctLeft = 200
rctTop = 675
rctWidth = 100
rctHeight = 100

QIDic = {}

Q = np.zeros(
    [5000, 3])  # number of states = (windowWidth / 8) * (windowHeight / circleYStep) * (windowWidth / rectWidth)