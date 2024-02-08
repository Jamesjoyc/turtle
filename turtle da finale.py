import turtle

turtle.fillcolor('black')
turtle.getscreen()
turtle.shape('circle')
turtle.pensize(4)
turtle.speed(-25)
turtle.shapesize(2)
turtle.penup()
turtle.goto(-375,275)
turtle.pendown()
turtle.forward(800)
turtle.left(90)
turtle.forward(200)
turtle.left(90)
turtle.forward(800)
turtle.left(90)
turtle.forward(200)
turtle.penup()

red = turtle.clone()
blue = turtle.clone()
green = turtle.clone()
grey = turtle.clone()
yellow = turtle.clone()
orange = turtle.clone()
pink = turtle.clone()
purple = turtle.clone()
lightgreen = turtle.clone()
lightblue = turtle.clone()


blue.pensize(4)
blue.color('blue')
blue.speed(-25)
blue.shapesize(2)
blue.penup()
blue.goto(-330,305)

green.pensize(4)
green.color('green')
green.speed(-25)
green.shapesize(2)
green.penup()
green.goto(-280,305)

grey.pensize(4)
grey.color('grey')
grey.speed(-25)
grey.shapesize(2)
grey.penup()
grey.goto(-230,305)

yellow.pensize(4)
yellow.color('yellow')
yellow.speed(-25)
yellow.shapesize(2)
yellow.penup()
yellow.goto(-180,305)

orange.pensize(4)
orange.color('orange')
orange.speed(-25)
orange.shapesize(2)
orange.penup()
orange.goto(-130,305)

pink.pensize(4)
pink.color('pink')
pink.speed(-25)
pink.shapesize(2)
pink.penup()
pink.goto(-80,305)

purple.pensize(4)
purple.color('purple')
purple.speed(-25)
purple.shapesize(2)
purple.penup()
purple.goto(-30,305)

red.pensize(4)
red.color('red')
red.speed(-25)
red.shapesize(2)
red.penup()
red.goto(20,305)

lightblue.pensize(4)
lightblue.color('lightblue')
lightblue.speed(-25)
lightblue.shapesize(2)
lightblue.penup()
lightblue.goto(70,305)

lightgreen.pensize(4)
lightgreen.color('lightgreen')
lightgreen.speed(-25)
lightgreen.shapesize(2)
lightgreen.penup()
lightgreen.goto(120,305)

turtle.goto(170,305)
def main():
    turtle.ondrag(dragging)
    turtle.mainloop()

def dragging(x, y):
    turtle.ondrag(None)
    turtle.setheading(turtle.towards(x, y))
    turtle.goto(x, y)
    turtle.ondrag(dragging)

turtle.listen()
main()
turtle.done()