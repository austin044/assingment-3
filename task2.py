import turtle

radius = float(input("How big do you want the bullseye?"))
targetx = int(input("Where would you like the target located on the x axis?:"))
targety = int(input("Where would you like the target located on the y axis?:"))

#black circle
newradius = radius + radius + radius + radius

turtle.penup()
turtle.goto(targetx, targety - newradius)
turtle.left(90)
turtle.right(90)
turtle.pendown()
turtle.color("black")
turtle.begin_fill()
turtle.circle(newradius)
turtle.end_fill()

# blue circle
newradius = newradius - radius

turtle.penup()
turtle.left(90)
turtle.forward(radius)
turtle.right(90)
turtle.pendown()
turtle.color("blue")
turtle.begin_fill()
turtle.circle(newradius)
turtle.end_fill()

#red circle
newradius = newradius - radius

turtle.penup()
turtle.left(90)
turtle.forward(radius)
turtle.right(90)
turtle.pendown()
turtle.color("red")
turtle.begin_fill()
turtle.circle(newradius)
turtle.end_fill()

#bullseye
turtle.penup()
turtle.left(90)
turtle.forward(radius)
turtle.right(90)
turtle.pendown()
turtle.color("yellow")
turtle.begin_fill()
turtle.circle(radius)
turtle.end_fill()

turtle.done()