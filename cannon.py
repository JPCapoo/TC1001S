#Juego del Tiro Parabólico (Randy)
from random import randrange
import turtle
from freegames import vector

ball = vector(-200, -200)
speed = vector(10, 10)
targets = []

def tap(x, y):
    "Respond to screen tap."
    if not inside(ball):
        ball.x = -199
        ball.y = -199
        speed.x = (x + 200) / 15
        speed.y = (y + 200) / 15

def inside(xy):
    "Return True if xy within screen."
    return -200 < xy.x < 200 and -200 < xy.y < 200

def draw():
    "Draw ball and targets."
    turtle.clear()

    for target in targets:
        turtle.goto(target.x, target.y)
        turtle.dot(20, 'blue')

    if inside(ball):
        turtle.goto(ball.x, ball.y)
        turtle.dot(6, 'red')

    turtle.update()

def move():
    "Move ball and targets."
    if randrange(40) == 0:
        y = randrange(-150, 150)
        target = vector(200, y)
        targets.append(target)

    for target in targets:
        target.x -= 5

    if inside(ball):
        speed.y -= 0.35
        ball.move(speed)

    dupe = targets.copy()
    targets.clear()

    for target in dupe:
        if abs(target - ball) > 13:
            targets.append(target)

    draw()

    # Ahora los objetivos se devuelven al pruncipio
    for target in targets:
        if not inside(target):
            target.x = 220

    turtle.ontimer(move, 50)

turtle.setup(420, 420, 370, 0)
turtle.hideturtle()
turtle.up()
turtle.tracer(False)
turtle.onscreenclick(tap)
move()
turtle.done()