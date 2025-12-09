huome = [9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 1, 1, 1, 1, 1]

while len(huome) >= 13:
    for i in range(len(huome) - 1):
        popped = False
        if huome[i] < huome[i+1]:
            huome.pop(i)
            popped = True
    print(popped)
    if popped == False:
        huome.pop(-1)

print(huome)