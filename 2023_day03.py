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


def get_digits_length(x, digits_row):

    x2 = x
    while x2 + 1 < len(digits_row):
        if digits_row[x2 + 1]:
            x2 += 1
        else:
            break
    return x2


def check_symbol_adjacency(y, x, d_length, symbols_matrix):


    d_length += 2
    #print("d_lenght: ", d_length)

    print(x, y, d_length, " START CHECKING ADJACENCY" )

    if x - d_length < 1:
        start_x = 0
    elif x == len(symbols_matrix[0][0]):
        d_length -= 1
        start_x = x - d_length
    else:
        start_x = x - d_length
    print("start_x = ", start_x)

    if y < 1:
        start_y = 0
    else:
        start_y = y - 1
        #print("y: ", y, " start_y: ", y - 1)
    #print("start_y = ", start_y)

    if y >= len(symbols_matrix) - 1:

        end_y = len(symbols_matrix[0][0]) - 1
        #print("LAST ROW", end_y)
    else:
        end_y = y + 1

    #print("end_y = ", end_y)

    """print("Checking x, y", matrix[x][0][y])
    if symbols_matrix[y][0][x]:
        print(matrix[y][0][x], "T R U E !")
        return True

    print("Checking start_x, y ", matrix[start_x][0][y])
    if symbols_matrix[y][0][start_x]:
        print(matrix[y][0][start_x], "T R U E !")
        return True

    print("Checking upper row", symbols_matrix[start_y][0], "from ", start_x, " to ", start_x + d_length, " !!!!!!")
    line_to_check = symbols_matrix[start_y][0]
    print("LENGTH :", len(symbols_matrix[start_y][0]))

    for i in range(start_x, (start_x + d_length)):
        print(line_to_check[i], end=" ")
        if line_to_check[i] == True:
            return True
    print()
    if any(line_to_check[i] for i in range(start_x, start_x + d_length)):
        print("FOUND ON UPPER ROW")
        return True

    print("Checking lower row", symbols_matrix[end_y][0])
    line_to_check = symbols_matrix[end_y][0]
    if any(line_to_check[i] for i in range(start_x, start_x + d_length)):
        print("FOUND ON LOWER ROW")
        return True"""

    # Loop y
    for i in range(start_y, (start_y + 3)):
        if i <= len(symbols_matrix[0][0]) - 1:
            line_to_check = symbols_matrix[i][0]
            indexes_to_check = line_to_check[start_x:(start_x + d_length + 1)]
            print(indexes_to_check)
            print("i", i, " <= ", len(digits[0][0]) - 1)

            if any(indexes_to_check):
                return True

    return False


def check_adjacent_symbols(digit_indexes, symbols):

    print(digit_indexes[0][0], digit_indexes[0][1], digit_indexes[-1][0], digit_indexes[-1][1], len(symbols[0]) - 1)
    # Set indexes in matrix
    if digit_indexes[0][0] > 0:
        start_y = digit_indexes[0][0] - 1
    else:
        start_y = 0

    if digit_indexes[0][1] > 0:
        start_x = digit_indexes[0][1] - 1
    else:
        start_x = 0

    if digit_indexes[-1][0] == len(symbols[0][0]) - 1:
        end_y = digit_indexes[-1][0]
    else:
        end_y = digit_indexes[-1][0] + 1

    if digit_indexes[-1][1] == len(symbols[0][0]) - 1:
        end_x = digit_indexes[-1][1]
    else:
        end_x = digit_indexes[-1][1] + 1
    print(start_y, start_x, end_y, end_x)
    # Compare masks
    print("Checking area")
    area_to_check = []
    for y in range(start_y, end_y + 1):
        ff = symbols[y][0][start_x: end_x + 1]
        area_to_check.append(ff)
    print(area_to_check)




def check_digits(matrix, digits, symbols, accpted):

    for row_y in range(len(digits[0])):
        digit_indexes = []
        digit_value = 0
        #print(matrix[0][0][-5])
        #print(row_y)
        for column_x in range(len(digits[0][0])):

            # If it's a digit
            #print(digits[0][row_y][column_x])
            if digits[0][row_y][column_x]:
                # Add coordinates to list
                digit_indexes.append((row_y, column_x))
                # Add value from cell
                digit_value = (digit_value * 10) + int(matrix[0][row_y][column_x])

            # If end of row or if last one not a digit
            if column_x == len(digits[0]) - 1 or not digits[0][row_y][column_x]:
                if len(digit_indexes) > 0:
                    if check_adjacent_symbols(digit_indexes, symbols):
                        accpted.append(digit_value)
                    digit_indexes = []
                    digit_value = 0


test = '226.241.893%..........257..312............69........792............/...........+...................$257..................790........./...184'
list_i = []
#print(test.split())
for i in test:
    list_i.append(i)
#print(list_i)

matrix = []
for line in Test_Lines2:
    row = []
    cleaned = line.split('\n')[0]
    #print(cleaned)
    row.append([*cleaned])
    matrix.append(row)

matrix = np.array(matrix)

#digits = check_pattern(matrix, digit_pattern)
#symbols = check_pattern(matrix, symbols_pattern)
#periods = check_pattern(matrix, periods_pattern)


for row in matrix:

    print(row)
    #for column in row:
        
# Vectorizing the function
vectorized_check = np.vectorize(check_pattern)

# Applying the regex pattern to the entire matrix
digits = vectorized_check(matrix, digit_pattern)
symbols = vectorized_check(matrix, symbols_pattern)
periods = vectorized_check(matrix, periods_pattern)

print(len(symbols))
#input()

digits_numbers = []

digits_counter = 0

digit_number = 0

print(symbols)
print(digits)
print(matrix)
#print(symbols)


check_digits(matrix, digits, symbols, digits_numbers)
"""
for i in range(len(matrix)):
    print("ROW ", i)
    digit_number = 0
    for j in range(len(matrix[0][0])):
        print("COLUMN ", j, " of ", len(digits[0][0]) - 1)
        #print(matrix[i][0][j], end=" ")

        # If it's a digit
        if digits[i][0][j]:
            digit_number = (digit_number * 10) + int(matrix[i][0][j])
            #print("making digit number: ", digit_number)

        # If it's not a digit
        elif not digits[i][0][j]:

            # Check if digit is bigger than 0
            if digit_number >= 1:
                #print("check adjacency", i, j, digit_number, len(str(digit_number)))

                # Check if adjacent symbols
                if check_symbol_adjacency(i, j, len(str(digit_number)) - 1, symbols):
                    digits_numbers.append(digit_number)
                    #print(digit_number)

                    print("APPEND", digit_number)
                digit_number = 0
            print()

        # Check if it's the end of the row
        if j == len(digits[0][0]) - 1:
            #print("END OF ROW")
            if digit_number >= 1:
                #print("check adjacency", i, j, digit_number, len(str(digit_number)) - 1)
                if check_symbol_adjacency(i, j, len(str(digit_number)) - 1, symbols):
                    digits_numbers.append(digit_number)
                    #print(digit_number)
                digit_number = 0
            print()
        else:
            print(j, " is less than ", len(digits[0][0]) - 1)




    print()

#print(matrix[0][0])
"""

print(digits_numbers)
print(sum(digits_numbers))

#for i in range(len(digits_numbers)):
#    print(len(str(digits_numbers[i])))