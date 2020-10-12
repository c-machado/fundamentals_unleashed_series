import sys

n = 50

data = []

for i in range(n):
    # Number of elements
    a = len(data)

    # Actual size in bytes
    b = sys.getsizeof(data)

    print('Length: {0:3d}; size in bytes: {1:4d}'. format(a, b))
    data.append(n)





