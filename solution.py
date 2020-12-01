
with open("data.txt", "r") as data:
    numbers = [int(line) for line in data.readlines()]

# 2 Numbers
for i in numbers:
    if (2020 - i) in numbers:
        print(i * (2020-i))
        break

# 3 Numbers
for i in numbers:
    for j in numbers:
        if (2020 - (i+j)) in numbers:
            print(i * j * (2020 - (i+j)))
            break
