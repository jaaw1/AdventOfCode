testdata = open('2025_day02_test.txt', 'r')
data = open('2025_day2_text.txt', 'r')
TestLines = testdata.readlines()
Lines = data.readlines()


def split_and_check(id):
    id_a, id_b = str(id)[:len(str(id)) // 2], str(id)[len(str(id)) // 2:]
    if id_a == id_b:
        return 1
    else:
        return 0


def multiples_check(id, rounds):
    x = len(str(id))
    if x < rounds:
        return 0
    elif x % rounds != 0:
        return 0
    else:
        round_len = x // rounds
        parts = [str(id)[i:i+round_len] for i in range(0, x, round_len)]

        for y in range(1, len(parts)):

            if parts[y] != parts[0]:

                return 0

        return 1


def loop(separated):
    counter = 0
    for i in range(len(separated)):

        id = separated[i]
        start, end = id.split("-")[0], id.split("-")[1]
        # print(start, end)

        for x in range(int(start), int(end) + 1):
            multi_counter = 0
            multi_counter += split_and_check(x)
            multi_counter += multiples_check(x, 3)
            multi_counter += multiples_check(x, 5)
            multi_counter += multiples_check(x, 7)
            if multi_counter > 0:
                counter += x

    print(counter)


separated = TestLines[0].split(",")
loop(separated)

separated = Lines[0].split(",")
loop(separated)