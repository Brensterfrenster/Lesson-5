from turtle import *

Rocksteady = Turtle()

Rocksteady.color("Red")
Rocksteady.pensize(6)
Rocksteady.speed(0)
Rocksteady.shape("turtle")

def drawHexagon(side):
	for x in range (6):
		Rocksteady.forward(side)
		Rocksteady.left(60)

drawHexagon(50)
drawHexagon(75)
drawHexagon(100)
drawHexagon(125)
drawHexagon(150)
drawHexagon(175)
drawHexagon(200)

mainloop()