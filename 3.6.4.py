words = ["composition", "of", "list", "traversed", "and", "early", "exit", "block", "create", "write", "first"]
count = 0

for word in words:
    if len(word) == 5:
        count = count + 1

print(count)
