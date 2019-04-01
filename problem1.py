from turtle import *

cuff = Turtle()

cuff.color("red")
cuff.pensize(6)
cuff.speed(0)
cuff.shape("turtle")

def DrawWheel():
	for x in range(3):
		cuff.forward(100)
		cuff.left(120)

DrawWheel()

mainloop()