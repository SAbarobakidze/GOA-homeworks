from turtle import *


#we want to paimt a house 
speed(30)
width(7)


color("pink")
begin_fill()
forward(200)
left(90)
forward(200)
left(90)


forward(200)
left(90)

forward(200)
left(90)
end_fill()

forward(70)
color("red")
begin_fill()
left(90)
forward(120)
right(90)
forward(60)
right(90)
forward(120)
end_fill()

penup()
goto(200, 200)
pendown()

color("green")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

penup()
goto(20, 130)
pendown()

color("brown")
right(150)
forward(40)
right(90)
forward(40)
right(90)
forward(40)
right(90)
forward(40)
right(90)
forward(20)
right(90)
forward(40)
left(90)
forward(20)
left(90)
forward(20)
left(90)
forward(40)


penup()
goto(180, 130)
pendown()


right(90)
forward(40)
right(90)
forward(40)
right(90)
forward(40)
right(90)
forward(40)
right(90)
forward(20)
right(90)
forward(40)
left(90)
forward(20)
left(90)
forward(20)
left(90)
forward(40)


exitonclick()