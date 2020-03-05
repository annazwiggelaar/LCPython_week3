import turtle
window = turtle.Screen()
tess = turtle.Turtle()
tess.shape("turtle")
tess.speed(0)

tess.penup()
tess.backward(100)
tess.pendown()

for _ in range(3):
    tess.forward(40)
    tess.left(120)

for _ in range(4):
    tess.forward(80)
    tess.left(90)

for _ in range(6):
    tess.forward(120)
    tess.left(60)

for _ in range(8):
    tess.forward(160)
    tess.left(45)

window.mainloop()
