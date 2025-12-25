import numpy as np
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

print(create_3d_vectors(TestLines))



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

    def add_to_group(self, data):
        self.data.append(data)

