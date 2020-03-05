length_a = float(input("What is the length of side a?"))
length_b = float(input("What is the length of side b?"))
length_c = float(input("What is the length of side c?"))

compare_c_squared = (length_a ** 2) + (length_b ** 2)
c_squared = length_c ** 2

compare_b_squared = (length_a ** 2) + (length_c ** 2)
b_squared = length_b ** 2

compare_a_squared = (length_b ** 2) + (length_c ** 2)
a_squared = length_a ** 2

threshold = 1e-7
if abs(compare_c_squared - c_squared) < threshold:
    print("True")
elif abs(compare_b_squared - b_squared) < threshold:
    print("True")
elif abs(compare_a_squared - a_squared) < threshold:
    print("True")
else:
    print("False")