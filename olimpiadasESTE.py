import turtle

pen = turtle.Turtle()
pen.speed(0.5)

#blue
pen.color('#0081C8')
pen.pensize(5)
pen.up()
pen.setpos(-35, 95)
pen.down()
r = 50
pen.circle(r,)

#black
pen.color('#000000')
pen.pensize(5)
pen.up()
pen.setpos(80, 95)
pen.down()
r = 50
pen.circle(r)

#red
pen.color('#EE334E')
pen.pensize(5)
pen.up()
pen.setpos(195, 95)
pen.down()
r = 50
pen.circle(r)



#yellow
pen.color('#FCB131')
pen.pensize(5)
pen.up()
pen.setpos(25, 45)
pen.down()
r = 50
pen.circle(r)


#green
pen.color('#00A651')
pen.pensize(5)
pen.up()
pen.setpos(135, 45)
pen.down()
r = 50
pen.circle(r)

#sobreposicao 


#azul 
pen.color('#0081C8')
pen.pensize(5)
pen.up()
pen.setpos(-35, 95)
pen.down()

r = 50
pen.circle(r,-275)

pen.color('#EE334E')
pen.pensize(5)
pen.up()
pen.setpos(245, 140)
pen.down()
r = 50
pen.circle(r,-100)

#black
pen.color('#000000')
pen.pensize(5)
pen.up()
pen.setpos(67, 97)
pen.down()
r = 50
pen.circle(r)

#green
pen.color('#00A651')
pen.pensize(5)
pen.up()
pen.setpos(123, 47)
pen.down()
r = 50
pen.circle(r, -100)

#yellow 
pen.color('#FCB131')
pen.pensize(5)
pen.up()
pen.setpos(-20, 117)
pen.down()
r = 50
pen.circle(r, -115)

#azul 
pen.color('#0081C8')
pen.pensize(5)
pen.up()
pen.setpos(3, 177)
pen.down()

r = 50
pen.circle(r,-80)


# Hide the turtle cursor
pen.hideturtle()

# Keep the window open
turtle.done()
screen.mainloop()
