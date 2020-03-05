import turtle
window = turtle.Screen()
tess = turtle.Turtle()
tess.shape("turtle")
tess.speed(2)

tess.penup()
tess.forward(100)
tess.pendown()

angles = [160, -43, 270, -97, -43, 200, -940, 17, -86]

for _ in angles:
    if _ > 0:
        tess.left(_)
        tess.forward(100)
    elif _ < 0:
        tess.right(_)
        tess.forward(100)

heading = (160 + -43 + 270 + -97 + -43 + 200 + -940 + 17 + -86) % 360
print("The drunk pirate's heading is", heading)

window.mainloop()