#Juego Pintando
"""
Ejercicios:
1. Un color nuevo
2. Dibujar un círculo
3. Completar el rectángulo
4. Completar el triángulo
"""

from math import hypot

import turtle

from freegames import vector


def line(start, end):
    """Draw line from start to end."""
    turtle.up()
    turtle.goto(start.x, start.y)
    turtle.down()
    turtle.goto(end.x, end.y)


def square(start, end):
    """Draw square from start to end."""
    turtle.up()
    turtle.goto(start.x, start.y)
    turtle.down()
    turtle.begin_fill()

    for count in range(4):
        turtle.forward(end.x - start.x)
        turtle.left(90)

    turtle.end_fill()


def newcircle(start, end):
    """Punto 2: Se obtiene la distancia del click 1 al 2 con la 
    función hypot, se redondea a un decimal, y se utiliza ese
    resultado en la función por defecto de la tortuga."""
    turtle.up()
    turtle.goto(start.x, (start.y + (start.y / 2)))
    radius = round(hypot((start.x - end.x),(start.y - end.y)), 1)
    turtle.begin_fill()
    turtle.circle(radius, 360)
    turtle.end_fill()


def rectangle(start, end):
    """Punto 3: Se usa la misma lógica del cuadrado solo que, en este
    caso, el ciclo solo itera 2 veces y utiliza tanto la diferencia
    en x como en y."""
    turtle.up()
    turtle.goto(start.x, start.y)
    turtle.down()
    turtle.begin_fill()

    for count in range(2):
        turtle.forward(end.x - start.x)
        turtle.left(90)
        turtle.forward(end.y - start.y)
        turtle.left(90)

    turtle.end_fill()


def triangle(start, end):
    """Punto 4: Misma lógica del cuadrado, pero teniendo en cuenta sus
    diferencias "trigonométricas". Es un triángulo equilátero"""
    turtle.up()
    turtle.goto(start.x, start.y)
    turtle.down()
    turtle.begin_fill()

    for count in range(3):
        turtle.forward(end.x - start.x)
        turtle.left(120)

    turtle.end_fill()


def tap(x, y):
    """Store starting point or draw shape."""
    start = state['start']

    if start is None:
        state['start'] = vector(x, y)
    else:
        shape = state['shape']
        end = vector(x, y)
        shape(start, end)
        state['start'] = None


def store(key, value):
    """Store value in state at key."""
    state[key] = value
    
def color(value):
    """Punto 1: Aquí se cambian el color de la pluma y el de relleno 
    (en el caso de las figuras)."""
    turtle.pencolor(value)
    turtle.fillcolor(value)

state = {'start': None, 'shape': line}
turtle.setup(420, 420, 370, 0)
turtle.onscreenclick(tap)
turtle.listen()
turtle.onkey(turtle.undo, 'u')
turtle.onkey(lambda: color('black'), 'k')
turtle.onkey(lambda: color('white'), 'w')
turtle.onkey(lambda: color('green'), 'g')
turtle.onkey(lambda: color('blue'), 'b')
turtle.onkey(lambda: color('red'), 'R')
turtle.onkey(lambda: store('shape', line), 'l')
turtle.onkey(lambda: store('shape', square), 's')
turtle.onkey(lambda: store('shape', newcircle), 'c')
turtle.onkey(lambda: store('shape', rectangle), 'r')
turtle.onkey(lambda: store('shape', triangle), 't')
turtle.done()