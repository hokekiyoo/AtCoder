"""
累積和っぽい

始点と終点の"2"つを指定しなければいけない
⇨二次元累積和ってやつ。

参考
https://qiita.com/drken/items/56a6b68edef8fc605821
"""

"""
N,M,Q = map(int,input().split())
A = [[0 for i in range(N+1)] for j in range(N+1)]
Acum = [[0 for i in range(N+1)] for j in range(N+1)]

for _ in range(M):
    L,R = map(int,input().split())
    A[L-1][R-1] += 1

#2次元累積和
for i in range(N):
    for j in range(N):
        Acum[i+1][j+1] = Acum[i][j+1] + Acum[i+1][j] - Acum[i][j] + A[i][j]

# print(Acum)
for _ in range(Q):
    p,q= map(int,input().split())
    A = Acum[q][q]-Acum[p-1][q]-Acum[q][p-1]+Acum[p-1][p-1]
    print(A)
"""

### いもす法　https://imoz.jp/algorithms/imos_method.html
import numpy as np
N,M,Q = map(int,input().split())
A = np.array([0 for i in range(N+1)])

for _ in range(M):
    L,R = map(int,input().split())
    A[L:R] += 1


# print(A)
for _ in range(Q):
    p,q= map(int,input().split())

