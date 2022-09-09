from turtle import Turtle, Screen
import random
color_list = [(236, 224, 80), (197, 7, 71), (195, 164, 13), (201, 75, 15), (231, 54, 132), (110, 179, 216), (217, 163, 101), (27, 105, 168), (35, 186, 109), (19, 29, 168), (13, 23, 66), (212, 135, 177), (233, 223, 7), (199, 33, 132), (13, 183, 212), (230, 166, 199), (126, 189, 162), (8, 49, 28), (40, 132, 77), (128, 219, 232), (58, 12, 25), (67, 22, 7), (114, 90, 210), (146, 216, 199), (179, 17, 8), (233, 66, 34)]

draw = Turtle()
draw.speed("fastest")
draw.hideturtle()
draw.pu()
draw.goto(-200, -200)
draw.pd()
screen = Screen()
screen.colormode(255)

for i in range(10):
    if i % 2 == 0:
        draw.setheading(0)
    else:
        draw.setheading(180)
    for j in range(9):
        draw.dot(20, random.choice(color_list))
        draw.pu()
        draw.forward(50)
        draw.pd()
    draw.dot(20, random.choice(color_list))

    draw.pu()
    draw.setheading(90)
    draw.forward(50)

screen.exitonclick()
