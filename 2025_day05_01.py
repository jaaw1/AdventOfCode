import numpy as np

testdata = open('2025_day05_test.txt', 'r')
data = open('2025_day05_text.txt', 'r')
TestLines = testdata.readlines()
Lines = data.readlines()
#a = Lines.replace("\n", "")
#print(a)

def create_fresh_id_array(data):


    fresh = np.empty([0,2]).astype(int)
    available = []
    line_split = False
    fresh = []
    for line in data:
        a = line.replace("\n", "")

        if len(a) > 0:
            if line_split:
                #print("r")
                available.append(int(a))
                #print(available)
            else:
                fre = a.split('-')
                start, end = int(fre[0]), int(fre[1])
                limits = (start, end)

                fresh.append(limits)
        else:
            line_split = True

            #print("Split")

    return fresh, available


def count_fresh_ingredients(fresh_limits, avalaible):
    total_fresh = 0

    for x in range(len(avalaible)):
        fresh = False
        for y in range(len(fresh_limits)):
            if avalaible[x] >= fresh_limits[y][0]:
                if avalaible[x] <= fresh_limits[y][1]:
                    fresh = True
                    total_fresh += 1
            if fresh:
                break
    return total_fresh




fresh_limits, available_ingrediments = create_fresh_id_array(Lines)

print(fresh_limits)
print(available_ingrediments)

print(count_fresh_ingredients(fresh_limits, available_ingrediments))
