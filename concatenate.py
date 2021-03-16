import numpy as np

n, m, p = map(int, input().split())
inputgiven1 = np.array((input().strip().strip() for i in range(n)))
inputgiven2 = np.array((input().strip().strip() for i in range(m)))
newarr = np.concatenate(inputgiven1, inputgiven2)