file = open('2022_02_input.txt', 'r')
file2 = open('2022_02_test.txt', 'r')
file3 = open('2022_02_test2.txt', 'r')
Lines = file.readlines()

"""
A = ROCK
B = PAPER
C = SCISSORS

Y = PAPER 2
X = ROCK 1
Z = SCISSORS 3

WIN = 6
DRAW = 3
LOOSE = 0

"""


total_points = 0

line_count = 0
enemy = ''
you = ''
# Strips the newline character
for line in Lines:
    line_count += 1
    for word in line.split():
        if word.upper() == 'A' or word.upper() == 'B' or word.upper() == 'C':
            enemy = word
        else:
            you = word

            if enemy.upper() == 'A':
                if you.upper() == 'X':  # DRAW
                    total_points += (3 + 1)
                elif you.upper() == 'Y':  # WIN
                    total_points += (6 + 2)
                elif you.upper() == 'Z':  # LOOSE
                    total_points += (0 + 3)
                else:
                    print("ERROR", line_count)

            elif enemy.upper() == 'B':
                if you.upper() == 'X':  # LOOSE
                    total_points += (0 + 1)
                elif you.upper() == 'Y':  # DRAW
                    total_points += (3 + 2)
                elif you.upper() == 'Z':  # WIN
                    total_points += (6 + 3)
                else:
                    print("ERROR", line_count)

            elif enemy.upper() == 'C':   # C
                if you.upper() == 'X':  # WIN
                    total_points += (6 + 1)
                elif you.upper() == 'Y':  # LOOSE
                    total_points += (0 + 2)
                elif you.upper() == 'Z':  # DRAW
                    total_points += (3 + 3)
                else:
                    print("ERROR", line_count)

            else:
                print("ENEMY ERROR", line_count)
print(total_points)
