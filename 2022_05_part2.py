import numpy as np
import string

file = open('2022_05_input.txt', 'rb')
file2 = open('2022_05_test.txt', 'rb')

Lines = file.readlines()
columns = [[], [], [], [], [], [], [], [], []]
uppercase_alphabet = list(string.ascii_uppercase)

phase = 0

row = []
for line in Lines:

    row.append(str(line))
    row = row[0]

    if phase == 0:

        row = row.split('\\')[0]
        row = row.split("b'")[1]

        if line.strip():
            column_index = 0
            counter = 1
            for i in range(len(row)):
                if row[i] in uppercase_alphabet:
                    column_index = int(counter / 4)
                    columns[column_index].append(row[i])
                counter += 1

            print(row)
            row = []
        else:
            phase += 1
            row = []

    elif phase == 1:
        #print(row)

        row = row.split('\\')[0]
        row = row.split("b'")[1]
        row = row.split(' ')



        var_move = int(row[1])

        var_from = int(row[3])

        var_to = int(row[5])

        print(var_move, var_from, var_to)

        mover = []

        for h in range(var_move):
            mover.insert(0, columns[var_from - 1].pop(0))

        for g in range(var_move):
            columns[var_to - 1].insert(0, mover.pop(0))
        print(columns[0], columns[1], columns[2])
        print(row)
        row = []

print(len(columns))
for j in range(len(columns)):

    print(columns[j][0], end="")
    #input()

