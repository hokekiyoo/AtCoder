"""
https://atcoder.jp/contests/abc085/tasks/abc085_d
貪欲
"""

import math 
N, H  = map(int, input().split())
As = []
Bs = []
for i in range(N):
    a,b  = map(int, input().split())
    As.append(a)
    Bs.append(b)

cnt = 0
Bs = [0] + sorted(Bs)
b = Bs.pop()
a = max(As)
while H > 0 and b > a:
    # print(a,b)
    H -= b #投げつけるパターン
    cnt += 1
    b = Bs.pop()
cnt += max(0,int(math.ceil(H / a)))

print(cnt)


