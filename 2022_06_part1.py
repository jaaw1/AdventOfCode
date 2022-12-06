file = open('2022_06_input.txt', 'rb')
file2 = open('2022_06_test.txt', 'rb')


def check_signal(signal):

    index = -1

    four_char = ''

    for i in range(len(signal)):
        four_char += signal[i]

        if len(four_char) > 4:
            four_char = four_char[1:]

        if len(four_char) == 4:
            letter_count = 0
            for letter in four_char:
                letter_count += four_char.count(letter)

            if letter_count < 5:
                index = i + 1
                break
    print(four_char)
    return index


Lines = file.readlines()

for line in Lines:
    signal = str(line)
    signal = signal.split("'")[1]


print(check_signal(signal))
