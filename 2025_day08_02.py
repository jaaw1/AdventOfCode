

import numpy as np
from scipy.spatial.distance import pdist


def create_3d_vectors(data):
    vectors = []
    for line in data:
        line = line.strip().split(',')
        line_vector = np.array(line, dtype=int)
        vectors.append(line_vector)

    return np.array(vectors)


testdata = open('2025_day08_test.txt', 'r')
data = open('2025_day08_text.txt', 'r')
TestLines = testdata.readlines()
Lines = data.readlines()

points = create_3d_vectors(Lines)
# --------------------------------------------------
# Setup
# --------------------------------------------------

N = len(points)
distances = pdist(points)

# Indices for condensed distance array
i_idx, j_idx = np.triu_indices(N, k=1)

# Sort all pairs by distance (shortest → longest)
order = np.argsort(distances)

# --------------------------------------------------
# Union–Find
# --------------------------------------------------

parent = list(range(N))

def find(x):
    while parent[x] != x:
        parent[x] = parent[parent[x]]
        x = parent[x]
    return x

def union(a, b):
    ra, rb = find(a), find(b)
    if ra == rb:
        return False
    parent[rb] = ra
    return True

# --------------------------------------------------
# Kruskal: track the LAST successful merge
# --------------------------------------------------

last_pair = None
last_distance = None

for k in order:
    i = i_idx[k]
    j = j_idx[k]

    if union(i, j):
        last_pair = (i, j)
        last_distance = distances[k]

# --------------------------------------------------
# Result
# --------------------------------------------------

i, j = last_pair
p1 = points[i]
p2 = points[j]

print("Last connected pair (MST edge):")
print("Index pair:", i, j)
print("Coordinates:")
print(p1)
print(p2)
print("Distance:", last_distance)
print("Answer: ", p1[0] * p2[0])
