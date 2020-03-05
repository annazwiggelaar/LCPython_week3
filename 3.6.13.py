n = 3478
count = 0

while n != 0:
    if n % 2 == 0:
        count = count + 1
        n = n // 10
    elif n % 2 != 0:
        n = n // 10
print(count)