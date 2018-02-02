class Circle:
    '''
    Aquí no hay ningún objeto Circle en Pygame. Esta clase compensaría eso.
     Es mucho más fácil trabajar con él que especificar las coordenadas xey cada vez
    :var circleX
    :var circleY
    '''

    def __init__(self, circleX, circleY):
        self.circleX = circleX
        self.circleY = circleY

class State:
    '''
    esta clase contendría la instantánea del juego,
    utilizada por el alumno q para indexar su tabla,
    así como la función de recompensa para determinar la
    recompensa de ese estado en particular.

    :var rectPosition
    :var circlePosition
    '''

    def __init__(self, rect, circle):
        self.rect = rect
        self.circle = circle