import numpy as np

N,M,C = map(int, input().split())
B = input().split()
Bs = np.array([float(b) for b in B])
A = np.zeros((N,M))
for i in range(N):
    A_i = input().split()
    A_i = [float(a) for a in A_i]
    A[i] = A_i
W = np.dot(A,Bs.T)
print(len(W[W+C>0]))
