file = open('2022_04_input.txt', 'rb')
file2 = open('2022_04_test.txt', 'rb')

Lines = file.readlines()


overlap = 0

for line in Lines:
    overlapping = False

    part_1, part_2 = str(line).split(",")

    elf_1 = part_1.split("b'")[1]
    elf_2 = part_2.split('\\')[0]

    elf_1_f, elf_1_l = elf_1.split('-')
    elf_2_f, elf_2_l = elf_2.split('-')

    elf_1_first = int(elf_1_f)
    elf_1_last = int(elf_1_l)

    elf_2_first = int(elf_2_f)
    elf_2_last = int(elf_2_l)

    #print(elf_1, " --- ", elf_2)

    while True:
        if elf_1_first < elf_2_first:  # first start smaller
            if elf_1_last >= elf_2_last:  # first end bigger or equal
                overlapping = True
                print("* ", elf_1, " overlapping ", elf_2)

        elif elf_1_first == elf_2_first or elf_1_last == elf_2_last:  # start equal - always overlap
            overlapping = True
            print("** ", elf_1, " overlapping ", elf_2)

          # == elf_2_first < elf_1_first:
        elif elf_1_first > elf_2_first:
            print(elf_1_first, ">", elf_2_first, elf_1_first > elf_2_first)
            if elf_1_last < elf_2_last:
                overlapping = True
                print("*** ", elf_1, " overlapping ", elf_2)


        if overlapping:
            overlap += 1
        break



print("Overlap: ", overlap)