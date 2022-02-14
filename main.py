import turtle  #1. import modules
import random

#Part A
window = turtle.Screen()  # 2.  Create a screen
window.bgcolor('lightblue')

michelangelo = turtle.Turtle()  # 3.  Create two turtles
leonardo = turtle.Turtle()
michelangelo.color('orange')
leonardo.color('blue')
michelangelo.shape('turtle')
leonardo.shape('turtle')

michelangelo.up()  # 4.  Pick up the pen so we don’t get lines
leonardo.up()
michelangelo.goto(-100, 20)
leonardo.goto(-100, -20)

## 5. your code goes here
leonardo.forward(58)
michelangelo.forward(96)
michelangelo.goto(-100, 20)
leonardo.goto(-100, -20)
for x in range(10):
    turtleranges = random.randrange(0, 10)
    turtleranges2 = random.randrange(0, 10)
    michelangelo.forward(turtleranges)
    leonardo.forward(turtleranges2)
michelangelo.goto(-100, 20)
leonardo.goto(-100, -20)

# Part B - complete part B here

michelangelo.down()
triangleturning = 360 / 3
length = 50
for x in range(3):
    michelangelo.forward(length)
    michelangelo.left(triangleturning)

michelangelo.up()

michelangelo.forward(60)

michelangelo.down()

squareturning = 360 / 4
for x in range(4):
    michelangelo.forward(length)
    michelangelo.left(squareturning)

michelangelo.up()

michelangelo.forward(90)

michelangelo.down()

hexagonturning = 360 / 6
for x in range(6):
    michelangelo.forward(length)
    michelangelo.left(hexagonturning)

michelangelo.up()

michelangelo.forward(120)

michelangelo.down()

nonagonturning = 360 / 9
for x in range(9):
    michelangelo.forward(length)
    michelangelo.left(nonagonturning)

michelangelo.up()

michelangelo.forward(200)

michelangelo.down()

dodecagonturning = 360 / 12
for x in range(12):
    michelangelo.forward(length)
    michelangelo.left(dodecagonturning)

window.exitonclick()
