from operator import mul
from functools import reduce

N,K = map(int, input().split())
mod = 10**9 +7

if N - K > K - 1:
    m = K
else:
    m = N - K + 1

def cmb(n,r):
    r = min(n-r,r)
    if r == 0: return 1
    over = reduce(mul, range(n, n - r, -1))
    under = reduce(mul, range(1,r + 1))
    return over // under

for i in range(1,K+1):
    if i <= m:
        a = cmb(K-1, i-1)%mod
        b = cmb(N-K+1, N-K-i+1)%mod
        print(a*b%mod)
    else:
        print(0)