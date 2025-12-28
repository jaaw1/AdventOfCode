import numpy as np
import math
from streamlit.runtime.stats import group_stats

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

points = create_3d_vectors(Lines)

print(points)


p1 = np.array((1, 2, 3))
p2 = np.array((1, 1, 1))

d = np.linalg.norm(p1 - p2)
print(d)
"""
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
        return any(np.array_equal(vector, x) for x in self.data)


    def __str__(self):
        return f'Size: {self.size}\\nLast: {self.data[-1]}'


d = Groups(list([points[0], points[1]]), 1)
print(d)

r = d.shortest_distance_to_vector_in_group(points[2])
print(r)

h = d.is_vector_in_this_group(points[0])
print(h)

hh = d.is_vector_in_this_group(points[8])
print(hh)

group_all = Groups(list(points[:]), 0)
print(group_all)
for i in range(len(points)):
    vector = points[i]
    print(vector)
    input("wait")