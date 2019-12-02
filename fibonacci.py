import turtle as t
from math import pi


def draw_shape(scale_prev, scale_num):
    '''draws a square with side scale_num. The fourth side of the square will be attached to the square for the previous
    number in the sequence'''
    x.backward(scale_prev)
    x.right(angle)
    for i in range(2):
        x.forward(scale_num)
        x.left(angle)
    x.forward(scale_num)


def draw_spiral(scale_num):
    '''draws a half semicircle (quad) with the radius scale_num '''
    circumference = pi * scale_num / 2
    plot = circumference/angle
    x._tracer(15)
    for j in range(angle):
        x.forward(plot)
        x.left(1)


def fibo_spiral():
    '''draws a spiral; representing the fibonacci series'''
    x.penup()
    x.setposition(-scale, 0)
    x.seth(0)
    x.pendown()
    x.pencolor("red")
    prev = 0
    num = 1
    x.right(angle)
    for i in range(n):
        scale_num = num * scale
        draw_spiral(scale_num)
        prev, num = num, prev + num


def fibo_plot():
    '''draws continuous squares with varied lengths that represents fibonacci series'''
    prev = 0
    num = 1
    x.pencolor("blue")
    x.backward(num * scale)
    for i in range(n):
        scale_prev = prev * scale
        scale_num = num * scale
        draw_shape(scale_prev, scale_num)
        prev, num = num, prev+num


scale = 10
angle = 90
n = int(input('Enter the number of iterations (must be between 2 and 8): '))
x = t.Turtle()
x._tracer(1)
if n > 1 and n < 9:
    t.title("Visualization of Fibonacci series")
    fibo_plot()
    fibo_spiral()
else:
    print("Please enter valid number of iterations (between 2 and 8")
t.done()
