import turtle
window = turtle.Screen()
window.bgcolor("lightgreen")
tess = turtle.Turtle()
tess.shape("turtle")
tess.color("blue")

tess.stamp()

for _ in range(12):
    tess.penup()
    tess.forward(150)
    tess.stamp()
    tess.backward(150)
    tess.right(30)
    tess.pendown()

tess.shape("classic")

for _ in range(12):
    tess.penup()
    tess.forward(120)
    tess.stamp()
    tess.backward(120)
    tess.right(30)
    tess.pendown()

tess.hideturtle()

window.mainloop()

