import turtle as tr
import random as rnd

    
    


shape = input('Enter which shape/triangle?(s/t)')
tr.speed(10000)
if shape == 's':
    for j in range(100):
        tr.penup()
        x_position = rnd.randint(-400, 300)
        y_position = rnd.randint(-200, 200)
        tr.goto(x_position, y_position)
        tr.pendown()
        for i in range(4):
            tr.fd(150)
            tr.lt(90)
if shape == 't':
    for j in range(100):
        tr.penup()
        x_position = rnd.randint(-400, 300)
        y_position = rnd.randint(-200, 200)
        tr.goto(x_position, y_position)
        tr.pendown()
        for i in range(3):
            tr.fd(150)
            tr.lt(120)


tr.done()

