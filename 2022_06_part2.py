file = open('2022_06_input.txt', 'rb')
file2 = open('2022_06_test.txt', 'rb')


def check_signal(signal):

    index = -1

    fourteen_char = ''

    for i in range(len(signal)):
        fourteen_char += signal[i]

        if len(fourteen_char) > 14:
            fourteen_char = fourteen_char[1:]

        if len(fourteen_char) == 14:
            letter_count = 0
            for letter in fourteen_char:
                letter_count += fourteen_char.count(letter)

            if letter_count < 15:
                index = i + 1
                break
    print(fourteen_char)
    return index


Lines = file.readlines()

for line in Lines:
    signal = str(line)
    signal = signal.split("'")[1]


print(check_signal(signal))