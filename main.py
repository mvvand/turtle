import math
import turtle

turtle.shape('turtle')
turtle.speed(4)


def square():
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(100)


def circle():
    for i in range(0, 360):
        turtle.forward(1)
        turtle.left(1)


def triangle():
    turtle.forward(200)
    turtle.left(120)
    turtle.forward(200)
    turtle.left(120)
    turtle.forward(200)


def hexagon():
    for i in range(0, 6):
        turtle.forward(200)
        turtle.left(60)


def spiral():
    i = 1
    for i in range(1000):
        turtle.forward(i * 0.01)
        turtle.left(1)


def square_spiral():
    i = 0
    for i in range(400):
        turtle.forward(5*i)
        turtle.left(90)
        i+=20


def ykazatel():
    turtle.penup()
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(180)
    turtle.pendown()

    turtle.forward(200)
    turtle.left(135)
    turtle.forward(100 * math.sqrt(2))
    turtle.left(90)
    turtle.forward(100 * math.sqrt(2))
    turtle.left(75)
    turtle.forward(200)
    turtle.left(120)
    turtle.forward(200)
    turtle.left(120)

    turtle.penup()
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(math.sqrt(3)/2 * 200)

    turtle.pendown()
    turtle.right(180)
    turtle.forward(math.sqrt(3)/2 * 200 + 100)


def star():
    for i in range(8):
        ykazatel()
        turtle.left(360/8)



#square()
#circle()
#triangle()
#hexagon()
#spiral()
#square_spiral()
#ykazatel()
star()