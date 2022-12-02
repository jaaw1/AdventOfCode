file = open('2022_02_input.txt', 'r')
file2 = open('2022_02_test.txt', 'r')
file3 = open('2022_02_test2.txt', 'r')
Lines = file.readlines()

"""
A = ROCK
B = PAPER
C = SCISSORS

Y = DRAW
X = LOOSE
Z = WIN

PAPER = 2
ROCK = 1
SCISSORS = 3

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

            if enemy.upper() == 'A':  # A = ROCK
                if you.upper() == 'X':  # LOSE  SCISSORS  0 + 3
                    total_points += (0 + 3)
                elif you.upper() == 'Y':  # DRAW  = ROCK 3 + 1
                    total_points += (3 + 1)
                elif you.upper() == 'Z':  # WIN  PAPER  6 + 2
                    total_points += (6 + 2)
                else:
                    print("ERROR", line_count)

            elif enemy.upper() == 'B':  # B = PAPER
                if you.upper() == 'X':  # LOSE  ROCK 0 + 1
                    total_points += (0 + 1)
                elif you.upper() == 'Y':  # DRAW = PAPER  3 + 2
                    total_points += (3 + 2)
                elif you.upper() == 'Z':  # WIN  SCISSORS  6 + 3
                    total_points += (6 + 3)
                else:
                    print("ERROR", line_count)

            elif enemy.upper() == 'C':   # C = SCISSORS
                if you.upper() == 'X':  # LOSE  PAPER  0 + 2
                    total_points += (0 + 2)
                elif you.upper() == 'Y':  # DRAW SCISSORS  3 + 3
                    total_points += (3 + 3)
                elif you.upper() == 'Z':  # WIN  ROCK 6 + 1
                    total_points += (6 + 1)
                else:
                    print("ERROR", line_count)

            else:
                print("ENEMY ERROR", line_count)
print(total_points)