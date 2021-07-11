import turtle

turtle.up()
turtle.goto(-50, 0)
turtle.down()


def draw_kite():
    turtle.left(50)
    for _ in range(4):
        turtle.forward(150)
        turtle.left(90)
    turtle.up()
    turtle.right(50)

def draw_circle():
    turtle.goto(-50, -50)
    turtle.down()
    turtle.circle(150, 360)
    turtle.up()

def draw_hexagon():
    turtle.goto(50, -100)
    turtle.down()
    for _ in range(6):
        turtle.left(360/6)
        turtle.fd(1250/6)
    turtle.up()

if __name__ == '__main__':
    draw_kite()
    draw_circle()
    draw_hexagon()
    turtle.done()
