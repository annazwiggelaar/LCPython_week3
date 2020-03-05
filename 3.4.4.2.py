days = [("Sunday", 0), ("Monday", 1), ("Tuesday", 2), ("Wednesday", 3), ("Thursday", 4), ("Friday", 5), ("Saturday", 6)]

starting_day = int(input("What is the starting day number?"))
length_stay = int(input("How many nights will you be away?"))

weeks_away = (starting_day + length_stay) % 7

for day, nr in days:
    if weeks_away == nr:
        print("You will return on", day)
