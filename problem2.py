from turtle import *

link = Turtle()

link.color('yellow')
link.pensize(6)
link.speed(0)
link.shape('turtle')

def drawTriangle():
	for x in range(3):
		link.forward(100)
		link.left(120)

def drawPizza():
	for x in range(18):
		drawTriangle()
		link.left(20)

drawPizza()

mainloop()