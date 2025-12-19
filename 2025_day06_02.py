import math

testdata = open('2025_day06_test.txt', 'r')
data = open('2025_day06_text.txt', 'r')
TestLines = testdata.readlines()
Lines = data.readlines()


def correct_line_lengths(lines):

    max_len = max(len(line) for line in lines)
    lines = [line.ljust(max_len) for line in lines]

    return lines


def calculations(data, method):

    if method == '*':
        return math.prod(data)
    elif method == '+':
        return sum(data)


lines = []

rows = []

for i, line in enumerate(Lines[:-1]):
    line = line.replace("\n", "")
    lines.append(line)
    row = list(line.split())

    rows.append(row)


math_methods = Lines[-1].split()

lines = correct_line_lengths(lines)


sums = []

u = len(math_methods) - 1
slicer = False
math_prob = []


for j in range(len(lines[1]) -1, -1, -1):

    num_string = ''
    for i in range(len(lines)):

        num_string += lines[i][j]
    num_string = num_string.strip()

    if num_string.isdigit():

        math_prob.append(int(num_string))
        if j == 0:
            sums.append(calculations(math_prob, math_methods[u]))
            break
    elif j == 0:

        sums.append((calculations(math_prob, math_methods)[0]))
    else:

        sums.append(calculations(math_prob, math_methods[u]))
        u -= 1
        math_prob = []

        if u == -1:

            break

print(sums)
print(sum(sums))
