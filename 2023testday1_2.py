def swap_words_with_digits(s, word_digit_dict):
    swapped_sentence = s  # Make a copy of the input string

    for word, digit in word_digit_dict.items():
        swapped_sentence = swapped_sentence.replace(word, str(digit))  # Replace word with its digit

    return swapped_sentence

# Example dictionary mapping words to digits
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

# Example string with concatenated words
sentence = "onethree4twoeightnine111"

# Swap words with their corresponding digits using the dictionary
result = swap_words_with_digits(sentence, word_to_digit)
print(result)

print("MORE\n")

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

# Example dictionary mapping words to digits
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

# Example string
sentence = "one 4two threeight four five"

# Swap words with their corresponding digits using the dictionary
result = swap_words_with_digits(sentence, word_to_digit)
result2 = swap_words_with_digits(result, word_to_digit)
print(result)
print(result2)
