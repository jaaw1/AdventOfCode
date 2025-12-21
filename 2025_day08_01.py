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