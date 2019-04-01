from turtle import *

Beebop = Turtle()

Beebop.color("Blue")
Beebop.pensize(6)
Beebop.speed(0)
Beebop.shape("turtle")

def drawHexagon():
	for x in range(6):
		Beebop.forward(100)
		Beebop.left(60)

drawHexagon()

mainloop()