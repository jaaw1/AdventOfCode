testdata = open('2025_day09_test.txt', 'r')
data = open('2025_day09_text.txt', 'r')
TestLines = testdata.readlines()
Lines = data.readlines()


def clean_lines(lines):
    clean_lines = []
    for line in lines:
        a = line.replace('\n', '')
        b = a.split(',')
        c, d = int(b[0]), int(b[1])
        clean_lines.append([c, d])

    return clean_lines


lines = clean_lines(Lines)
testlines = clean_lines(TestLines)

print(testlines)


def square_sizes(data):
    squares = []

    for i in range(len(data) -1):
        for j in range(i + 1, len(data)):
            a = abs(data[i][0] - data[j][0]) + 1
            b = abs(data[i][1] - data[j][1]) + 1
            squares.append(a*b)
    return squares

print(square_sizes(testlines))
squares = square_sizes((lines))
print(max(squares))