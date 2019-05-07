import numpy as np
N,M = map(int, input().split())
As, Bs = [], []
Cs = np.zeros((N,2))
for i in range(N):
    A, B = map(int, input().split())
    Cs[i] = [A,B]

C_sorted = Cs[Cs[:,0].argsort(), :]
value = 0
for a,b in C_sorted:
    M_tmp = M - b
    if M_tmp > 0:
        value += a*b
        M = M_tmp
    else:
        value += a*M
        break

print(value)