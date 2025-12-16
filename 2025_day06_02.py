import math
import numpy as np
testdata = open('2025_day06_test.txt', 'r')
data = open('2025_day06_text.txt', 'r')
TestLines = testdata.readlines()
Lines = data.readlines()


def find_max_length_of_strings_in_list(rows):
    max_length = []
    for row in rows:
        max_length.append(len(max(row, key=len)))

    return max(max_length)


def fill_dots_at_end(rows, max_len):
    for row in rows:
        for i in range(len(row)):
            row[i] += '.' * (max_len - len(row[i]))
        #print(row)


def correct_line_lengths(lines):

    max_len = max(len(line) for line in lines)
    lines = [line.ljust(max_len) for line in lines]

    print(lines)
    return lines

def check_column(x, depth, lines):
    test = False
    for i in range(depth):
        if lines[i][x] == ' ':
            if i == depth:
                return True
            else:
                test = check_column(x, depth - 1, lines)
        else:
            return False
    return test


def find_interval(lines):
    for i in range(1):
        for j in range(len(lines[i])):
            if lines[i][j] == ' ':
                print(j, check_column(j, len(lines) - 1, lines))

            print(lines[i][j], end="")
        print()


def calculations(data, method):

    if method == '*':
        return math.prod(data)
    elif method == '+':
        return sum(data)


def sum_of_columns(lines):
    sums = np.zeros((1,len(lines[0])))
    print(len(lines[0]), len(sums[0]))
    input(lines)
    print(sums.shape)

    for i in range(len(lines)):
        for j in range(len(lines[i])):
            print(j)
            if lines[i][j] != ' ':
                sums[0][j] += int(lines[i][j])

    print(sums)
lines = []
rows = []

for i, line in enumerate(TestLines[:-1]):
    line = line.replace("\n", "")
    lines.append(line)
    row = list(line.split())

    rows.append(row)


math_methods = TestLines[-1].split()

lines = correct_line_lengths(lines)
print(lines)
#print(rows)
#print(math_methods)
max_len = find_max_length_of_strings_in_list(rows)

#fill_dots_at_end(rows, max_len)

#find_interval(lines)

#sum_of_columns(lines)

sums = []

for u in range(len(math_methods) -1, -1, -1):
    math_prob = []
    slicer = False
    for j in range(len(lines[1]) -1, -1, -1):
        if slicer:
            break
        num_string = ''
        for i in range(len(lines)):

            num_string += lines[i][j]
        num_string = num_string.strip()
        if num_string.isdigit():
            math_prob.append(int(num_string))
        else:
            slicer = True
            sums.append(calculations(math_prob, math_methods[u]))



print(sums)