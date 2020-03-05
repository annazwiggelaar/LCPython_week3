numbers = [3, 5, 65, 234, 57, 89, 1, 34, 52, 108, 101]
total = 0

for number in numbers:
    if number % 2 == 0:
        total = total + number

print(total)
