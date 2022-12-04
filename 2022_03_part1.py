import string

file = open('2022_03_input.txt', 'rb')
file2 = open('2022_03_test.txt', 'rb')

Lines = file.readlines()
#print(Lines)
lowercase_alphabet = list(string.ascii_lowercase)
uppercase_alphabet = list(string.ascii_uppercase)

sum_of_characters = 0

for line in Lines:
    # Make line to a string without end-of-line things or such.
    d_string = str(line)
    separated_str = d_string.split("\\", 1)
    #print(separated_str)
    word = separated_str[0].split("b'")[1]
    print(word)

    #divide the word in two
    diiv = int(len(word) / 2)
    w1 = word[:diiv]
    w2 = word[diiv:]
    print(w1, w2)
    for i in range(len(w1)):
        if w1[i] in w2:
            print(w1[i])
            if w1[i] in lowercase_alphabet:
                sum_of_characters += lowercase_alphabet.index(w1[i]) + 1
                print(lowercase_alphabet.index(w1[i]) + 1)
            else:
                sum_of_characters += uppercase_alphabet.index(w1[i]) + 1 + 26
                print(uppercase_alphabet.index(w1[i]) + 1 + 26)
            break

    #print(n, w1, w2 + n)

print(sum_of_characters)