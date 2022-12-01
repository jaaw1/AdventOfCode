
file = open('2021_02_input.txt', 'r')
file2 = open('2021_02_test.txt', 'r')
Lines = file.readlines()

count = 0
vertical = 0
horizontal = 0
aim = 0
direction = 'UP'

# Strips the newline character
for line in Lines:
    for word in line.split():
        if word.isnumeric():
            if direction.upper() == 'UP':
                aim -= int(word)
            elif direction.upper() == 'DOWN':
                aim += int(word)
            else:
                horizontal += int(word)
                vertical += aim * int(word)
        else:
            direction = word

print(horizontal, vertical, horizontal*vertical)