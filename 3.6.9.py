numbers = [3, 5, 65, 234, 57, 89, 1, 34, 52, 108, 101]

for number in numbers:
    if number > 1:
       for i in range(2, number // 2):
           if number % i == 0:
               print(number, "False")
               break

       else: print(number, "True")

    else: print(number, "False")

