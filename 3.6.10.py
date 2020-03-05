import turtle
window = turtle.Screen()
anna = turtle.Turtle()
anna.shape("turtle")
anna.speed(1)

movement = [(160, 20), (-43, 10), (270, 8), (-43, 12)]

for angle, steps in movement:
    anna.left(angle)
    anna.forward(steps)

window.mainloop()
