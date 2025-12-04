a = [7, 6, 5, 4, 3, 2, 1, 0]

for i in range(4, -1, -1):
    print(a[i])


b = [(1, 2), (3, 4), (2, 3), (1, 2)]

c = list(set(tuple(b)))

print(c)
d = [[(1, 2), (3, 4)],[]]


e = [ele for ele in d if ele != []]
print(e)