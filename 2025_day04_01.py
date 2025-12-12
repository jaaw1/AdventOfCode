import numpy as np

#testdata = open('2025_day04_test.txt', 'r')
#data = open('2025_day04_text.txt', 'r')
#TestLines = testdata.readlines()
#Lines = data.readlines()
"""
TestData = np.loadtxt('2025_day04_test.txt', dtype=str)

A = np.array([list(row) for row in TestData])
print(A)
mask = (TestData == '@').astype(int)

p = np.pad(mask, 1)

shifts = [
    (0, 1), (0, -1), (1, 0), (-1, 0),
    (1, 1), (1, -1), (-1, 1), (-1, -1)
]

neighbor_counts = sum(p[1 + dx : 1 + dx + mask.shape[0], 1 + dy : 1 + dy + mask.shape[1]] for dx, dy in shifts)

print(neighbor_counts)
#
#print(TestData[0][4])

total_rolls = 0

# All but edges
for i in range(1, len(TestData)-1):
    #print(TestData[i])
    for j in range(1, len(TestData[i])-1):
        #print(TestData[i][j])
        count_paper = 0
        if TestData[i][j] == '@':
            for y in range(i-1, i+2):
                for x in range(j - 1, j + 2):
  #                  print(TestData[y][x])
                    if TestData[y][x] == '@':
                        if y != i and x != j:
                            count_paper += 1
                        #print(y, i, x, j, (y != i and x != j))
                #print(TestData[y][x])
                #input()

 #       print(i, j, count_paper)
        if count_paper < 4:
            total_rolls += 1

#print(total_rolls)


#print(mask)"""

import numpy as np

# Load file
with open('2025_day04_text.txt') as f:
    lines = [line.strip() for line in f]

# Convert to 2D character array
A = np.array([list(row) for row in lines])

# Make sure A is 2D even for a single line file
if A.ndim == 1:
    A = A.reshape(1, -1)

# Create mask
mask = (A == '@').astype(int)

# Pad
p = np.pad(mask, 1)

# Neighbor shifts
shifts = [
    (0,1), (0,-1), (1,0), (-1,0),
    (1,1), (1,-1), (-1,1), (-1,-1)
]

# Count neighbors
neighbor_counts = sum(
    p[1+dx:1+dx+mask.shape[0],
      1+dy:1+dy+mask.shape[1]]
    for dx, dy in shifts
)

#print(neighbor_counts)
#print()
filtered = neighbor_counts * mask

#print(filtered)

count_rolls = 0

for row in filtered:
    for item in row:
        if item > 0:
            if item < 4:
                count_rolls += 1

print(count_rolls)