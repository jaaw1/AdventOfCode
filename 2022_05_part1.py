import numpy as np
import string

file = open('2022_05_input.txt', 'rb')
file2 = open('2022_05_test.txt', 'rb')

Lines = file.readlines()
columns = [[],[],[],[],[],[],[],[],[]]
#print(len(columns))
uppercase_alphabet = list(string.ascii_uppercase)

row = []
for line in Lines:


    #print(type(line))
    #row.append(str(line).split(' '))
    row.append(str(line))
    row = row[0]
    row = row.split('\\')[0]
    row = row.split("b'")[1]

    if line.strip():
        #print(row, len(row))
        #input()
        column_index = 0
        counter = 1
        for i in range(len(row)):

            #print(counter)
            if row[i] in uppercase_alphabet:
                column_index = int(counter / 4)
                columns[column_index].append(row[i])
                print(row[i], column_index)

            counter += 1
        print(row)
        #print(len(row), counter)
        #for i in range(len(row)):
        #    print(i, row[i])


        row = []
    else:
        break

for j in range(len(columns)):

    print(columns[j])
    #input()

