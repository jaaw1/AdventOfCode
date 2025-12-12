import numpy as np


def count_neighbors(x, y, papers):
    #print("ROW ", x)
    count = 0
    for i in range(x-1, x + 2):
        #print("row ", i)
        for j in range(y - 1, y + 2):
            #if x == 10:
                #print("KYMPPIRIVI", x, y, i, j)
            #print("column ", j )
            if i == x:
                if j == y:
                    print("", end="")
                else:
                   count += papers[i][j]
            else:
                count += papers[i][j]
    if count < 4:
        #print(x, y, "COUNT")
        return 1

    return 0

# Load file
with open('2025_day04_text.txt') as f:
    lines = [line.strip() for line in f]

# Convert to 2D character array
A = np.array([list(row) for row in lines])

#print(A)

papers = (A == '@').astype(int)
row = A.shape[0]
column = A.shape[1] + 2

#print(row, column)
print(papers)
X = np.zeros(row,).astype(int)
Y = np.zeros((column, 1)).astype(int)
print(X)

papers = np.vstack((X, papers))
papers = np.vstack((papers, X))

papers = np.column_stack((Y, papers))
papers = np.column_stack((papers, Y))

print(papers)


removed_total = 0
rolls = 1
while rolls > 0:
    rolls = 0
    for i in range(1, row+1):
        #print("Row ", i, "/ Column ", end=" ")
        for j in range(1, column):
            if papers[i][j] == 1:
                print()
                #print("hit:", j, end=" ")
                fork = count_neighbors(i, j, papers)
                rolls += fork
                if fork > 0:
                    papers[i][j] = 0
    print(rolls)
            #print(i, j)
    removed_total += rolls
    #print()

print("ANSWER: ", removed_total)