N, M = map(int,input().split())
SWs = []
# 電球がどのスイッチに繋がっているか
from collections import defaultdict
d = defaultdict(list)
for i in range(N):
    d[i+1].append(0)


for i in range(M):
    As = list(map(int,input().split()))
    SWs.append(As[1:])
    for A in As[1:]:
        d[A].append(i+1)

# 正しい電球のON状態
ps = list(map(int,input().split()))
ans = 0

# スイッチ状態の全通り
for i in range(2**N):
    light = [0] * (M+1)
    flg = True
    x = bin(i)[2:]
    #調整
    a = "0"*(N-len(x))+x
    for i,s in enumerate(a):
        if int(s) == 0:
            for A in d[i+1]:
                light[A] += 1
    # print(a,light,ps)
    for p,l in zip(ps,light[1:]):
        if p != l%2:
            flg = False
    if flg:
        ans += 1

print(ans)