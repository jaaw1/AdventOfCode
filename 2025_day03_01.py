testdata = open('2025_day03_test.txt', 'r')
data = open('2025_day03_text.txt', 'r')
TestLines = testdata.readlines()
Lines = data.readlines()


def find_largest_joltage(data):
    joltage = 0
    for line in data:
        max_jolt = 0
        for i in range(len(line)-1):
            for j in range(i+1, len(line)-1):

                if int(line[i]+line[j]) > max_jolt:
                    max_jolt = int(line[i]+line[j])

        joltage += max_jolt

    print(joltage)


find_largest_joltage(TestLines)

find_largest_joltage(Lines)