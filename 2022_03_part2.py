import string

file = open('2022_03_input.txt', 'rb')
file2 = open('2022_03_test.txt', 'rb')

Lines = file.readlines()
#print(Lines)
lowercase_alphabet = list(string.ascii_lowercase)
uppercase_alphabet = list(string.ascii_uppercase)

sum_of_characters = 0

three_lines = []

for line in Lines:

    # Make line to a string without end-of-line things or such.
    d_string = str(line)
    separated_str = d_string.split("\\", 1)
    word = separated_str[0].split("b'")[1]

    three_lines.append(word)

    if len(three_lines) > 2:
        for j in range(len(three_lines[0])):
            if three_lines[0][j] in three_lines[1]:
                if three_lines[0][j] in three_lines[2]:
                    if three_lines[0][j] in lowercase_alphabet:
                        sum_of_characters += lowercase_alphabet.index(three_lines[0][j]) + 1
                    else:
                        sum_of_characters += uppercase_alphabet.index(three_lines[0][j]) + 1 + 26
                    three_lines.clear()
                    break



print(sum_of_characters)