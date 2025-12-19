
testdata = open('2025_day07_test.txt', 'r')
data = open('2025_day07_text.txt', 'r')
TestLines = testdata.readlines()
Lines = data.readlines()

beams = []
splits = 0


def clean_lines(lines):

    for line in lines:
        line = line.replace('\n', '')

    return lines


lines = clean_lines(Lines)
testlines = clean_lines(TestLines)


#for line in testlines:
    #print(line)

beams = []
split_counter = 0

for i in range(len(lines[0])):
    if lines[0][i] == 'S':
        beams.append(i)
        print(f'Starting point is {i}')
        break


for line in lines:
    new_beams = []
    #print(line)
    for beam in beams:
        #print(beam)
        if line[beam] == '^':
            split_counter += 1
            new_beams.append(beam - 1)
            new_beams.append(beam + 1)
        else:
            new_beams.append(beam)

    beams = list(set(new_beams))
    print(beams)

print(f'The beams split a total of {split_counter} times.')
