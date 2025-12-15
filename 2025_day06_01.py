import math
testdata = open('2025_day06_test.txt', 'r')
data = open('2025_day06_text.txt', 'r')
TestLines = testdata.readlines()
Lines = data.readlines()


def calculator(rows, mathods):

    total = 0

    for i in range(len(mathods)):
        new_line = []
        for j in range(len(rows)):
            new_line.append(rows[j][i])

        if mathods[i] == '*':
            total += math.prod(new_line)

        elif mathods[i] == '+':
            total += sum(new_line)

    return total


rows = []

for i, line in enumerate(Lines[:-1]):
    line = line.replace("\n", "")
    TestLines[i] = list(map(int, line.split()))
    row = TestLines[i]
    rows.append(row)


math_methods = Lines[-1].split()


print("Result: ", calculator(rows, math_methods))
