words = ["composition", "of", "list", "traversed", "and", "sam", "early", "exit", "block", "create", "write", "first"]
count = 0

for word in words:
    count = count + 1
    if word == "sam":
        break

print(count)
