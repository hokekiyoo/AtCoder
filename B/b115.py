import numpy as np

N = int(input())
ps = np.zeros(N)

for i in range(N):
    p = int(input())
    ps[i] = p

SUM = ps.sum() - ps.max()/2
print(int(SUM))