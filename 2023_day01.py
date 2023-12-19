import re


def numbers(s):
    #print(type(s))
    digits = re.findall(r"\d", s)
    if digits:
        final = int(str(digits[0]) + str(digits[-1]))
        #print(digits, final)
        return final
    return 0


def swap_words_with_digits(s, word_digit_dict):
    # Sort the word-digit dictionary by word length in descending order
    sorted_dict = {k: v for k, v in sorted(word_digit_dict.items(), key=lambda item: len(item[0]), reverse=True)}

    swapped_sentence = ""
    i = 0
    while i < len(s):
        found = False
        for word in sorted_dict:
            if s[i:i + len(word)] == word:
                swapped_sentence += str(sorted_dict[word])
                swapped_sentence += str(word[-1])
                i += len(word)
                found = True
                break
        if not found:
            swapped_sentence += s[i]
            i += 1

    return swapped_sentence


word_to_digit = {
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9,

}


data = open('day1_input.txt', 'r')
Lines = data.readlines()

test_data = open('test_data_day1.txt', 'r')
Test_Lines = test_data.readlines()

test2_data = open('test_data_day1_2.txt', 'r')
Test_Lines2 = test2_data.readlines()

total_sum = 0
test_sum = 0

for line in Test_Lines:
    test_sum += numbers(line)

print("####")
for line in Lines:
    total_sum += numbers(line)

print(test_sum)
print(total_sum)

print("PART 2\n")
test_sum = 0

final_sum = 0
for line in Test_Lines2:
    swapped = swap_words_with_digits(line, word_to_digit)
    swapped2 = swap_words_with_digits(swapped, word_to_digit)
    #print(swapped, numbers(swapped))
    test_sum += numbers(swapped2)

print(test_sum)

for line in Lines:
    swapped3 = swap_words_with_digits(line, word_to_digit)
    swapped4 = swap_words_with_digits(swapped3, word_to_digit)
    # print(swapped, numbers(swapped))
    final_sum += numbers(swapped4)

print(final_sum)

"""
import requests

url = 'https://adventofcode.com/2023/day/1/input'
r = requests.get(url, stream=True)

for line in r.iter_lines():
    if line: print(line)"""