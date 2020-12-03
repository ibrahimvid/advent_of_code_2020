with open("data.txt", "r") as data:
    passwords = [line for line in data.readlines()]

counter = 0
counter_2 = 0

for password in passwords:
    item = password.split(' ')
    min_max = item[0].split('-')
    low = int(min_max[0])
    high = int(min_max[1])
    letter = item[1][0]
    pwd = item[2].strip()

    # Problem 1
    if letter in pwd:
        if low <= pwd.count(letter) <= high:
            counter += 1

    # Problem 2
    if (pwd[low - 1] == letter or pwd[high - 1] == letter) and not(pwd[low - 1] == letter and pwd[high - 1] == letter):
        counter_2 += 1


print(counter)
print(counter_2)
