"""
DFSバージョン
"""
import sys

# DFSの再帰限界を増やす
sys.setrecursionlimit(10**6)

N = int(input())
nmax = 100001
# nmax = 10
# 第一成分にx,第二成分にyをぶち込んでいく。(二部グラフなので)
xys = [[[] for i in range(nmax)] for j in range(2)]

used = [[0 for i in range(nmax)] for j in range(2)]
# 読み込み
for _ in range(N):
    x, y = map(int, input().split())
    xys[0][x].append(y)
    xys[1][y].append(x)
# print(xys)

# 座標の切り替えをx = 1 or 0と1-xで行うのか、うまい！
# よく考えたらtrue/falseをひっくり返しているだけか。
def dfs(i, el=0):
    # el=0->x, el=1->y
    for i in xys[el][i]:
        if not used[1-el][i]:
            used[1-el][i] = True
            # 再帰
            dfs(i, 1-el)
            cnt[1-el] += 1

ans = 0
for i in range(nmax):
    # まだ行ったことがなくて空じゃないところ
    if xys[0][i] != [] and used[0][i] == 0:
        used[0][i] = 1
        cnt = [1,0]
        dfs(i,0)
        ans += cnt[0]*cnt[1]
print(ans-N)
