import numpy as np

#f = np.zeros(5)

#print(f)

data = [[['.', '.', '5', '0', '4', '.', '*']],
     [['*', '.', '1', '0', '2', '.', '.']],
     [['.', '.', '.', '.', '.', '.', '.']],
     [['.', '1', '0', '0', '.', '.', '.']],
     [['.', '.', '.', '.', '.', '.', '.']],
     [['.', '*', '.', '.', '.', '.', '.']],
     [['.', '.', '0', '.', '.', '.', '.']],
     [['.', '2', '0', '0', '.', '.', '.']]]

symbols = [[[False, False, False, False, False, False, True]],
 [[True, False, False, False, False, False, False]],
 [[False, False, False, False, False, False, False]],
 [[False, False, False, False, False, False, False]],
 [[False, False, False, False, False, False, False]],
 [[False, True, False, False, False, False, False]],
 [[False, False, False, False, False, False, False]],
 [[False, False, False, False, False, False, False]]]

digits = [[[False, False, True, True, True, False, False]],
 [[False, False, True, True, True, False, False]],
 [[False, False, False, False, False, False, False]],
 [[False,  True, True, True, False, False, False]],
 [[False, False, False, False, False, False, False]],
 [[False, False, False, False, False, False, False]],
 [[False, False, True, False, False, False, False]],
 [[False, True, True, True, False, False, False]]]


def merge_contiguous_digits(row):
    merged_cells = []
    merged_number = ''
    for cell in row:
        if cell.isdigit():
            merged_cells.append(cell)
            merged_number += cell
        elif merged_cells:
            # If consecutive digits end, merge them into a single number
            merged_number = int(merged_number)
            yield merged_cells, merged_number
            merged_cells = []
            merged_number = ''
    if merged_cells:
        # If the row ends with consecutive digits, merge them
        merged_number = int(merged_number)
        yield merged_cells, merged_number

def find_2_3_digit_numbers(data):
    numbers = {}  # Store 2-3 digit numbers and their positions
    for row_idx, row in enumerate(data):
        for merged_cells, number in merge_contiguous_digits(row[0]):
            if len(str(number)) == 2 or len(str(number)) == 3:
                for col_idx in range(len(row[0])):
                    if row[0][col_idx] in merged_cells:
                        numbers[(row_idx, col_idx)] = number
    return numbers


# Finding 2-3 digit numbers and checking adjacent coordinates
numbers = find_2_3_digit_numbers(data)
print(numbers)
for index, value in numbers.items():
    adjacent_symbols = merge_contiguous_digits(data)
    print(f"Number: {value}, Index: {index}, Adjacent Symbols: {adjacent_symbols}")

