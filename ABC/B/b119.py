import numpy as np
N = int(input())
vs = np.zeros(N)
for i in range(N):
    x,u = input().split()
    if u == "BTC":
        vs[i] = float(x)*380000.0
    elif u == "JPY":
        vs[i] = int(x)
sum_v = vs.sum()
print(sum_v)