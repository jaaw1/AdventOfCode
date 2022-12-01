file = open('2022_01_input.txt', 'r')
file2 = open('2022_01_test.txt', 'r')
Lines = file.readlines()

count = 0
elf_calories = 0
top_3_elves = [0, 0, 0]
last = 0
# Strips the newline character
for line in Lines:
    if not line.strip():

        if elf_calories > top_3_elves[0]:
            print(top_3_elves)
            top_3_elves[0] = elf_calories
            top_3_elves.sort()

        elf_calories = 0
    else:
        elf_calories += int(line)

if elf_calories > top_3_elves[0]:
    print(top_3_elves)
    top_3_elves[0] = elf_calories

print(sum(top_3_elves))