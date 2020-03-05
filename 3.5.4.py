numbers = [12, 10, 32, 3, 66, 17, 42, 99, 20]
total = 0

for number in numbers:
    total = total + number + number ** 2    # sum
    print(number, "\n", (number ** 2))

print("\nThe total is", total, "\n")

# new exercise with product
total = 1

for number in numbers:
    total = total * number * (number ** 2)
    print(number, "\n", (number ** 2))

print("\nThe total is", total)