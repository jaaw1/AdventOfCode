testdata = open('2025_day07_test.txt', 'r')
data = open('2025_day07_text.txt', 'r')
TestLines = testdata.readlines()
Lines = data.readlines()


def clean_lines(lines):

    for line in lines:
        line = line.replace('\n', '')

    return lines


lines = clean_lines(Lines)
testlines = clean_lines(TestLines)

starting_point = -1

beam_counter = [0]


for i in range(len(lines[0])):
    if lines[0][i] == 'S':
        starting_point = i
        print(f'Starting point is {i}')


        break

print(len(lines))

def beam_traverse(x, y):
    #Recursion. Ok for test data but too slow for the main data.

    print(x, y)
    if y == len(lines):
        beam_counter[0] += 1
        print(x, y, beam_counter)

    elif lines[y][x] == '^':
        #left
        beam_traverse(x-1, y+1)
        #right

        beam_traverse(x+1, y+1)
    else:
        #down straight
        beam_traverse(x, y+1)

#beam_traverse(starting_point, 0)

#print(beam_counter)

def beam_traverse_dp(start_x):
    height = len(lines)
    width = len(lines[0])

    # dp[y][x] = number of beams at position (x, y)
    dp = [[0] * width for _ in range(height + 1)]
    dp[0][start_x] = 1

    for y in range(height):
        for x in range(width):
            beams = dp[y][x]
            if beams == 0:
                continue

            if lines[y][x] == '^':
                if x - 1 >= 0:
                    dp[y + 1][x - 1] += beams
                if x + 1 < width:
                    dp[y + 1][x + 1] += beams
            else:
                dp[y + 1][x] += beams

    # All beams that reach beyond the last row
    return sum(dp[height])


total_routes = beam_traverse_dp(starting_point)
print(total_routes)