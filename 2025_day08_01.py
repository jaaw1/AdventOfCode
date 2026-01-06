import numpy as np
from scipy.spatial import cKDTree
from scipy.spatial.distance import pdist, squareform
from collections import defaultdict
#print(np.__version__)
import math
#from streamlit.runtime.stats import group_stats

testdata = open('2025_day08_test.txt', 'r')
data = open('2025_day08_text.txt', 'r')
TestLines = testdata.readlines()
Lines = data.readlines()

"""ss = np.array(([[1, 2, 3], [7, 8, 9]]))
print(ss)
sss = np.append(ss, np.array(([[4, 5, 6]])), axis=0)
print(sss)"""


def create_3d_vectors(data):
    vectors = []
    for line in data:
        line = line.strip().split(',')
        line_vector = np.array(line, dtype=int)
        vectors.append(line_vector)

    return np.array(vectors)


def merge_groups(groups, ind1, ind2):

    a, b = groups[ind1], groups[ind2]
    #print(len(a.data.shape))
    if len(a.data.shape) > 1:
        a.data = np.append(a.data, [b.data], axis=0)
    else:
        a.data = np.append([a.data], [b.data], axis=0)
    #print(len(a.data.shape))

    groups.pop(ind2)
    return a.data



points = create_3d_vectors(TestLines)



"""rem = np.array([points[0]])
input(rem)
drem = np.append(rem, np.array([points[1]]), axis=0)
input(drem)
mer = np.array([points[2]])
dmer = np.append(mer, np.array([points[3]]), axis=0)
print(dmer)
merde = np.append(drem, dmer, axis=0)
input(merde)"""



#print(points)

"""
p1 = np.array((1, 2, 3))
p2 = np.array((1, 1, 1))

d = np.linalg.norm(p1 - p2)
print(d)

import numpy as np
from sklearn.cluster import DBSCAN

# xyz points, shape (1000, 3)
points = np.random.rand(1000, 3)

db = DBSCAN(eps=0.05, min_samples=2).fit(points)
labels = db.labels_

print(labels)
"""
all_groups = []


class Groups:
    def __init__(self, data, group_id):
        self.data = data
        self.id = group_id
        self.size = len(self.data)


    def add_to_group(self, data):
        self.data.append(data)
        self.size = len(self.data)

    def shortest_distance_to_vector_in_group(self, vector):
        distances = []
        for item in self.data:
            distance = np.linalg.norm(item - vector)
            distances.append(distance)
            #print(distances)
        return min(distances)





    def is_vector_in_this_group(self, vector):
        print(self.data, vector, self.data == vector)
        return any(np.array_equal(vector, x) for x in self.data)


    def __str__(self):
        return f'Size: {self.size}  Last: {self.data[-1]}'


for i in range(len(points)):
    group = Groups(points[i], i)
    all_groups.append(group)



"""print(merge_groups(all_groups, 0, 1))
input("115 wait")"""


"""
for x in range(len(points)):

    nearest_group = 10000000
    nearest_id = 1001
    native = 1001

    # get native group
    for i in range(len(all_groups)):
        isit = all_groups[i].is_vector_in_this_group(points[x])
        print(isit, points[x], all_groups[i].data)
        if isit:
            native = i
            print("Native: ", native)
            break

    for y in range(len(all_groups)):
        if y == i:
            pass
        else:
            nearest = all_groups[y].shortest_distance_to_vector_in_group(points[x])
        if nearest < nearest_group:
            nearest_group == nearest
            nearest_id = y

    merge_groups(all_groups, native, nearest_id)
"""




"""d = Groups(list([points[0], points[1]]), 1)
print("rivi 129", d)
print("Name: ", type(d).__name__)
r = d.shortest_distance_to_vector_in_group(points[2])
print("rivi 132", r)

dd = Groups(list([points[0]]), 1)
print("rivi 135", dd.data[0])
print("rivi 136", d.is_vector_in_this_group(dd.data[0]))

ff = Groups(list([points[2], points[3]]), 1)
gg = Groups(list([points[4], points[5]]), 1)

all_groups.append(ff)
all_groups.append(gg)

#tt = ff.merge_groups(gg)
tt = merge_groups(all_groups, 0, 1)

print(tt)

h = d.is_vector_in_this_group(points[0])
print("rivi 146", h)

hh = d.is_vector_in_this_group(points[8])
print( "rivi 149", hh)

input("wait")"""
#group_all = Groups(list(points[:]), 0)
#print(group_all)

"""
for i in range(len(points)):
    vector = points[i]
    print(vector)
    reve = group_all.is_vector_in_this_group(vector)
    print(reve)

    #input("wait")"""

#e_points = np.random.rand(40, 3)
#print(e_points)

#CONTINUE HERE (SKIP THIS VERSION) NEW ONE UNDER

# 1. loop points
    #for every point, find its closest neighbor
# 2. Find group of closest neighbor
# 3 Find group of the point in the loop in turn
# 4. Merge these two groups

#

#for i in range(len(all_groups)):
#    print(all_groups[i].data)

#NEW VERSION
# 1 list of distances (pairs) ordered by the length (indices of the points in the points list)
# 2 (pick the 10 first (test) or 100 first and join them by the indices

# Compute all pairwise distances (condensed form)
distances = pdist(points)  # length = N*(N-1)/2

# Get indices that would sort distances
order = np.argsort(distances)

# Convert condensed indices → (i, j) pairs
pairs = []
N = len(points)

k = 0
for i in range(N):
    for j in range(i + 1, N):
        pairs.append((i, j))
        k += 1

# Closest pairs in order
closest_pairs = [(pairs[idx], distances[idx]) for idx in order]
print(closest_pairs)
parent = list(range(N))

size = [1] * N

a_pairs = np.array([])
"""
for pair in closest_pairs:
    a_pair = np.array([pair[0]])
    a_pairs = np.append(a_pairs, a_pair)


for pair in a_pairs:
    print(pair)
"""
# How to use this code? Is "pairs" in right format? Or "closest_pairs"?


def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])  # path compression
    return parent[x]


def union(a, b):
    root_a = find(a)
    root_b = find(b)

    if root_a == root_b:
        return  # already in the same group

    # union by size (attach smaller tree to larger)
    if size[root_a] < size[root_b]:
        root_a, root_b = root_b, root_a

    parent[root_b] = root_a
    size[root_a] += size[root_b]

for i, j in pairs:
    union(i, j)

for i in range(N):
    find(i)

group_sizes = [size[i] for i in range(N) if parent[i] == i]

largest_3 = sorted(group_sizes, reverse=True)[:3]
print(largest_3)

from collections import defaultdict

groups = defaultdict(list)

for i in range(N):
    root = find(i)
    groups[root].append(i)

# sizes
group_sizes = [len(g) for g in groups.values()]

[size[i] for i in range(N) if parent[i] == i]

print(sorted(group_sizes, reverse=True)[:3])


