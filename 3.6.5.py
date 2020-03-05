numbers = [3, 5, 65, 234, 57, 89, 1, 34, 52, 108, 101]
total = 0
once = False

for number in numbers:
    if number % 2 == 0 and not once:
        once = True
        continue
    total = total + number

print(total)
