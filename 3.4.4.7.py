length_a = int(input("What is the length of side a?"))
length_b = int(input("What is the length of side b?"))

c_squared = (length_a ** 2) + (length_b ** 2)
c = c_squared ** 0.5

print("The length of the hypotenuse is", c)
