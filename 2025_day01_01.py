data = open('2025_day01_01.txt', 'r')
Lines = data.readlines()

counter = 0

point = 50

for line in Lines:
    direction = line[0]
    amount = int(line[1:].replace("\n", ""))
    if direction == "L":
        for i in range(amount):
            point -= 1
            if point == -1:
                point = 99
    else:
        for i in range(amount):
            point += 1
            if point == 100:
                point = 0
    if point == 0:
        counter += 1


print(counter)



