import turtle
import math


def draw_square(a,b):
    x.backward(a * scale)
    x.right(90)
    x.forward(b * scale)
    x.left(90)
    x.forward(b * scale)
    x.left(90)
    x.forward(b * scale)


def draw_spiral(b):
    circumference = math.pi * b * scale / 2
    plot = circumference/90
    for j in range(90):
        x.forward(plot)
        x.left(1)


def fibo_spiral():
    x.penup()
    x.setposition(-scale, 0)
    x.seth(0)
    x.pendown()
    x.pencolor("red")

    a=0
    b=1
    x.right(90)
    for i in range(n):
        draw_spiral(b)
        a, b = b, a + b


def fibo_plot(n):
    a = 0
    b = 1
    x.pencolor("blue")
    x.backward(b * scale)
    for i in range(n):
        draw_square(a, b)
        a, b = b, a+b


scale = 10
n = int(input('Enter the number of iterations (must be > 0): '))
x = turtle.Turtle()
x.speed(1)
if n > 1:
    fibo_plot(n)
    fibo_spiral()
turtle.done()
