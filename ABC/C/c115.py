import numpy as np
N, K = map(int,input().split())
hs = np.zeros(N)
for i in range(N):
    hs[i] = int(input())

# sort
h_sorted = np.sort(hs)
min_delta = np.inf

# hmax-hminを求めていく
for i in range(N-K+1):
    delta = h_sorted[i+K-1] - h_sorted[i]
    if min_delta >= delta:
        min_delta = delta
print(int(min_delta))
    