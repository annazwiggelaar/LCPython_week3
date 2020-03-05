import turtle
window = turtle.Screen()
anna = turtle.Turtle()
anna.shape("turtle")
anna.speed(2)

movement = [(180, 100), (-90, 100), (-90, 100), (120, 100), (120, 100), (75, 141), (135, 100), (135, 141)]

for angle, steps in movement:
    anna.left(angle)
    anna.forward(steps)

window.mainloop()
