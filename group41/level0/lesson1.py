from turtle import *

#we want to paint a house

#step 1: draw a square
speed(30)
width(7)
color("red")
forward(200)
left(90) 

forward(200)
left(90)

forward(200)
left(90) 

forward(200)
left(90)

# end of scuare

#drawing a door

forward(70)

color("green")
begin_fill()
left(90)

forward(120)
right(90)

forward(60)
right(90)

forward(120)
end_fill()

penup()
goto(200,200)
pendown()

color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()


goto(200,200)


left(30)
forward(10)
color("black")

begin_fill()
right(90)
forward(60)

left(90)
forward(40)

left(90)
forward(60)

end_fill()
color("red")

left(90)
forward(50)
left(90)
forward(200)
left(90)
forward(10)
left(90)
color("black")
begin_fill()
forward(60)
right(90)
forward(40)
right(90)
forward(60)
end_fill()



exitonclick()