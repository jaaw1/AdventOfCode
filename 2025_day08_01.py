import numpy as np
import math
#from streamlit.runtime.stats import group_stats

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


def merge_groups(groups, ind1, ind2):
    print(ind1, ind2)
    groups[ind1].data.append(groups[ind2].data)

    print(groups[ind1])
    groups.pop(ind2)



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
        print(self.data, vector, self.data == vector)
        return any(np.array_equal(vector, x) for x in self.data)


    def __str__(self):
        return f'Size: {self.size}  Last: {self.data[-1]}'


for i in range(len(points)):
    group = Groups(points[i], i)
    all_groups.append(group)

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
d = Groups(list([points[0], points[1]]), 1)
print(d)
print("Name: ", type(d).__name__)
r = d.shortest_distance_to_vector_in_group(points[2])
print(r)

ff = Groups(list([points[2], points[3]]), 1)
gg = Groups(list([points[4], points[5]]), 1)

tt = ff.merge_groups(gg)
print(tt)

h = d.is_vector_in_this_group(points[0])
print(h)

hh = d.is_vector_in_this_group(points[8])
print(hh)

group_all = Groups(list(points[:]), 0)
print(group_all)
for i in range(len(points)):
    vector = points[i]
    print(vector)
    input("wait")"""