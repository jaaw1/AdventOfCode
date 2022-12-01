file = open('2022_01_input.txt', 'r')
file2 = open('2022_01_test.txt', 'r')
Lines = file.readlines()

count = 0
elf_calories = 0
most_calories = 0
last = 0
# Strips the newline character
for line in Lines:
    if not line.strip():
        if elf_calories > most_calories:
            most_calories = elf_calories
        elf_calories = 0
    else:
        elf_calories += int(line)

print(most_calories)