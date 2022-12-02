file = open('2021_01_input.txt', 'r')
file2 = open('2021_01_test.txt', 'r')
Lines = file.readlines()

count = 0
larger = 0
previous = []
this = []
three = 0

# Strips the newline character
for line in Lines:
    count += 1
    if count > 3:

        previous = this.copy()
        this.pop(0)

        this.append(int(line))

        if sum(this) > sum(previous):
            larger += 1

        print(this, previous)

    else:
        this.append(int(line))


print(larger)