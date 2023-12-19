import numpy as np
import re

data = open('day3_input.txt', 'r')
Lines = data.readlines()

test_data = open('test_data_day3.txt', 'r')
Test_Lines = test_data.readlines()

test_data2 = open('test_data_day3_own.txt', 'r')
Test_Lines2 = test_data2.readlines()


# Regex patterns
digit_pattern = r'\d+'  # Matches one or more digits
symbols_pattern = r'[^\w\s.]'
periods_pattern = r'[.]'


# Function to check for matches using regex
def check_pattern(item, pattern):
    return bool(re.match(pattern, str(item))) if isinstance(item, str) else False


def check_first_last(number, digits):
    # Check if first row
    if number[0][0] == 0:
        first_r = True
    else:
        first_r = False

    # Check if first column
    if number[0][1] == 0:
        first_c = True
    else:
        first_c = False

    # Check if end of row
    if number[-1][1] == len(digits[0][0]) - 1:
        last_c = True
    else:
        last_c = False

    # Check if last row
    if number[0][0] == len(digits) - 1:
        last_r = True
    else:
        last_r = False

    return first_r, first_c, last_r, last_c


def check_adjacency(number, value, symbols, adjacency):

    first_r, first_c, last_r, last_c = check_first_last(number, adjacency)

    # print("\nCHECKING    \nfirst_r: ", first_r, "\nfirst_c: ", first_c, "\nlast_r: ", last_r, "\nlast_c: ", last_c)

    if first_r:
        y = 0
        y2 = 1
    else:
        y = number[0][0] - 1
        y2 = number[0][0] + 1

    if first_c:
        x = 0
        x2 = number[-1][1] + 1
    else:
        x = number[0][1] - 1
        x2 = number[-1][1] + 1

    if last_r:
        y = number[0][0] - 1
        y2 = number[0][0]

    if last_c:
        x = number[0][1] - 1
        x2 = number[-1][1]



    print(f'From {y},{x} to {y2},{x2}')
    for i in range(len(adjacency)):
        for j in range(len(adjacency[0][0])):
            adjacency[i][0][j] = False

    """for row in adjacency:
        print(row)
    print()"""

    for i in range(y, y2 + 1):
        for j in range(x, x2 + 1):
            adjacency[i][0][j] = True

    """for i_row in range(len(adjacency)):
        print(adjacency[i_row], "      ", symbols[i_row])

    print()"""
    """for row in symbols:
        print(row)"""

    has_common_true = np.any(np.logical_and(symbols, adjacency))

    if has_common_true:
        print("Has common TRUE", value)
        return value
    else:
        print("No common TRUE", value)
        return 0

def find_numbers(matrix, digits, symbols):

    first_r = True
    first_c = True
    last_r = False
    last_c = False

    number = []
    number_value = 0
    total_value = 0

    for i in range(len(digits)):



        for j in range(len(digits[0][0])):
            print(digits[i][0][j], end=" ")

            # Check if first row
            if i == 0:
                first_r = True
            else:
                first_r = False

            # Check if first column
            if j == 0:
                first_c = True
            else:
                first_c = False

            # Check if end of row
            if j == len(digits[0][0]) - 1:
                last_c = True
            else:
                last_c = False

            # Check if last row
            if i == len(digits) - 1:
                last_r = True
            else:
                last_r = False

            # Check if True (is digit)
            if digits[i][0][j]:
                number.append((i, j))
                number_value *= 10
                number_value += int(matrix[i][0][j])

                if last_c:
                    print("Check adjacency for ", number_value, number, end=" ")
                    total_value += check_adjacency(number, number_value, symbols, adjacency_check_map)
                    #input("press enter")
                    number_value = 0
                    number = []
            else:
                if number_value > 0:
                    print("Check adjacency for ", number_value, number, end=" ")
                    total_value +=  check_adjacency(number, number_value, symbols, adjacency_check_map)
                    #input("press enter")
                    number_value = 0
                    number = []


        print(f'Total value: {total_value}')


# Creating the Matrix
matrix = []
for line in Lines:
    row = []
    cleaned = line.split('\n')[0]
    #print(cleaned)
    row.append([*cleaned])
    matrix.append(row)

matrix = np.array(matrix)


for row in matrix:
    print(row)
    # for column in row:

# Vectorizing the function
vectorized_check = np.vectorize(check_pattern)

# Applying the regex pattern to the entire matrix
digits = vectorized_check(matrix, digit_pattern)
symbols = vectorized_check(matrix, symbols_pattern)
periods = vectorized_check(matrix, periods_pattern)
adjacency_check_map = vectorized_check(matrix, periods_pattern)


#print(digits, "\n")
find_numbers(matrix, digits, symbols)

