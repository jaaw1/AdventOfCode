file = open('2021_01_input.txt', 'r')
file2 = open('2021_01_test.txt', 'r')
Lines = file.readlines()

count = 0
larger = 0
last = 0
# Strips the newline character
for line in Lines:
    count += 1
    if count > 1:
        if int(line) > last:
            larger += 1
    last = int(line)

print(larger)