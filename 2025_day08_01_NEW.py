import numpy as np
from scipy.spatial.distance import pdist, squareform


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


# -------------------------------------
# Parameters
# -------------------------------------
X = 1000                      # number of closest pairs to connect
#points = np.asarray(points)  # ensure numpy array
points = create_3d_vectors(Lines)

N = len(points)

# -------------------------------------
# Union-Find (Disjoint Set)
# -------------------------------------
parent = list(range(N))
size = [1] * N

def find(x):
    while parent[x] != x:
        parent[x] = parent[parent[x]]  # path compression
        x = parent[x]
    return x

def union(a, b):
    ra, rb = find(a), find(b)
    if ra == rb:
        return
    if size[ra] < size[rb]:
        ra, rb = rb, ra
    parent[rb] = ra
    size[ra] += size[rb]

# -------------------------------------
# Step 1: Pairwise distances
# -------------------------------------
distances = pdist(points)   # condensed distance matrix

# -------------------------------------
# Step 2: Get indices of X smallest distances
# -------------------------------------
idx = np.argpartition(distances, X)[:X]

# -------------------------------------
# Step 3: Convert condensed indices → (i, j)
# -------------------------------------
pairs = np.array(np.triu_indices(N, k=1)).T
closest_pairs = pairs[idx]

# -------------------------------------
# Step 4: Union only those X pairs
# -------------------------------------
for i, j in closest_pairs:
    union(i, j)

# -------------------------------------
# Step 5: Collect group sizes
# -------------------------------------
groups = {}
for i in range(N):
    r = find(i)
    groups[r] = groups.get(r, 0) + 1

group_sizes = sorted(groups.values(), reverse=True)

# -------------------------------------
# Step 6: Print 3 largest groups
# -------------------------------------
print(group_sizes[:3])

distances = pdist(points)
k = np.argmax(distances)
i, j = np.triu_indices(len(points), k=1)
print(points[i[k]][0] * points[j[k]][0])