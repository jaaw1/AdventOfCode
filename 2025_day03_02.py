testdata = open('2025_day03_test.txt', 'r')
data = open('2025_day03_text.txt', 'r')
TestLines = testdata.readlines()
Lines = data.readlines()


def find_joltage(line):
    while len(line) >= 13:
        for i in range(len(line) - 1):
            popped = False
            #print("hep ", i, line[i], line[i+1], line)
            if line[i] < line[i + 1]:
                line.pop(i)
                popped = True
                break
        #print(popped)
        if popped == False:
            line.pop(-1)

    return line


sum = 0

for line in TestLines:
    line = line.replace("\n", "")
    line = list(line)
    sum += int(''.join(find_joltage(line)))
    #print(''.join(find_joltage(line)))

print(sum)
print("3121910778619")

sum = 0
for line in Lines:
    line = line.replace("\n", "")
    line = list(line)
    sum += int(''.join(find_joltage(line)))
print(sum)