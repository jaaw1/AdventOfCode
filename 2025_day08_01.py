import numpy as np

testdata = open('2025_day08_test.txt', 'r')
data = open('2025_day08_text.txt', 'r')
TestLines = testdata.readlines()
Lines = data.readlines()


def create_3d_vectors(data):
    vectors = []
    for line in data:
        line = line.strip().split(',')
        line_vector = np.array(line, dtype=int)
        vectors.append(line_vector)

    return np.array(vectors)

print(create_3d_vectors(TestLines))



p1 = np.array((1, 2, 3))
p2 = np.array((1, 1, 1))

d = np.linalg.norm(p1 - p2)
print(d)


class Vector_groups:
    def __init__(self, data):
        self.group = np.array([data])


