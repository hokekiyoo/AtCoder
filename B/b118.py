import numpy as np
N, M = map(int,input().split())
kinds = np.zeros(M)
for _ in range(N):
    inputs = input().split()
    K = inputs[0]
    A = inputs[1:]
    for a in A:
        kinds[int(a)-1] += 1
N = len(kinds[np.where(kinds==N)])
print(N)
