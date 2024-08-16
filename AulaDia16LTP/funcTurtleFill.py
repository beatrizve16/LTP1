import turtle as tl

screen = tl.Screen()

tl.bgcolor("beige")
tl.pensize(5)
tl.color("#6B705C", "#B7B7A4")
tl.begin_fill()
tl.circle(100)
tl.end_fill()



tl.begin_fill()
for i in range (4):
    tl.forward(100)
    tl.left(90)
tl.end_fill()


tl.hideturtle()
tl.done
tl.mainloop()
