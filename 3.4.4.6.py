numbers = [83, 75, 74.9, 70, 69.9, 65, 60, 59.9, 55, 50, 49.9, 45, 44.9, 40, 39.9, 2, 0]

for number in numbers:
    if number >= 75:
        print("Your mark is", number, ", your grade is", "First")
    if 70 <= number < 75:
        print("Your mark is", number, ", your grade is", "Upper Second")
    if 60 <= number < 70:
        print("Your mark is", number, ", your grade is", "Second")
    if 50 <= number < 60:
        print("Your mark is", number, ", your grade is", "Third")
    if 45 <= number < 50:
        print("Your mark is", number, ", your grade is", "F1 Supp")
    if 40 <= number < 45:
        print("Your mark is", number, ", your grade is", "F2")
    if number < 40:
        print("Your mark is", number, ", your grade is", "F3")
        
