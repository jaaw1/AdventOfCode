testdata = open('2025_day02_test.txt', 'r')
data = open('2025_day2_text.txt', 'r')
TestLines = testdata.readlines()
Lines = data.readlines()


def split_and_check(id):
    id_a, id_b = str(id)[:len(str(id)) // 2], str(id)[len(str(id)) // 2:]
    if id_a == id_b:
        return id
    else:
        return 0


def loop(separated):
    counter = 0
    for i in range(len(separated)):

        id = separated[i]
        start, end = id.split("-")[0], id.split("-")[1]
        # print(start, end)

        for x in range(int(start), int(end) + 1):
            counter += split_and_check(x)

    print(counter)


separated = TestLines[0].split(",")
loop(separated)

separated = Lines[0].split(",")
loop(separated)