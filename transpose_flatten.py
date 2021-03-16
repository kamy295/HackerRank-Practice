import numpy as np
n, m = map(int, input().split())
inputgiven = np.array([input().strip().split() for i in range(n)], int)
print(inputgiven.transpose())
print(inputgiven.flatten())
