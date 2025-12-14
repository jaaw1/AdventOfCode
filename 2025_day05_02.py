import time

testdata = open('2025_day05_test.txt', 'r')
data = open('2025_day05_text.txt', 'r')
TestLines = testdata.readlines()
Lines = data.readlines()


def create_fresh_id_limits_list(data):

    line_split = False
    fresh = []

    for line in data:
        a = line.replace("\n", "")

        if len(a) > 0:
            if line_split:
                break

            else:
                fre = a.split('-')
                start, end = int(fre[0]), int(fre[1])
                limits = [start, end]

                fresh.append(limits)

        else:
            line_split = True

    return fresh


def combine_overlapping(limits):

    no_more_overlapping = []

    while len(limits) > 1:

        new_limit = limits.pop(0)
        start_a, end_a = new_limit[0], new_limit[1]
        found_new_overlaps = True

        while found_new_overlaps:

            found_new_overlaps = False
            for x in range(len(limits)):

                start_b, end_b = limits[x][0], limits[x][1]
                if start_a <= start_b <= end_a:

                    new_limit = [min(start_a, start_b), max(end_a, end_b)]
                    start_a, end_a = new_limit[0], new_limit[1]
                    found_new_overlaps = True

                    limits.pop(x)
                    break
                elif start_a <= end_b <= end_a:

                    new_limit = [min(start_a, start_b), max(end_a, end_b)]
                    start_a, end_a = new_limit[0], new_limit[1]
                    found_new_overlaps = True
                    limits.pop(x)
                    break

            if len(limits) < 1:
                break
        # When no more overlap matches with new_limit, it is moved to list "no_more_overlapping"
        no_more_overlapping.append(new_limit)

        if len(limits) == 0:
            break

    # When there is only one item left in list "limits", it is added to list "no_more_overlapping"
    if len(limits) > 0:
        no_more_overlapping.append(limits[-1])
    else:
        return no_more_overlapping


def count_limits(limits):
    counter = 0

    for limit in limits:

        counter += ((limit[1]+1) - limit[0])


    return counter


start = time.time()

fresh_limits = create_fresh_id_limits_list(Lines)

print("Create list:", time.time() - start)

fresh_limits.sort()

print("Sorted list:", time.time() - start)

final_limits = combine_overlapping(fresh_limits)
print("OUT OF FUNCTION:")

print("Final result:", count_limits(final_limits), " ID's")
print("Total time:", time.time() - start)