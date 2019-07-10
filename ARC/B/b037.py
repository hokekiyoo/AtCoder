
from collections import deque

# 木構造を作る
N, M = map(int, input().split())
G = [[] for i in range(N)]

for i in range(M):
    u,v = map(int,input().split())
    G[u-1].append((v-1))
    G[v-1].append((u-1))

used = [0] * N
def dfs(G, v,pre_v):
    global flg
    # vを訪問済みにする
    used[v] += 1
    #グラフ中の次のVについて
    for next_v in G[v]:
        # 無向グラフ分.しゃーなし
        if pre_v == next_v:
            continue
        # それ以外で地雷踏む
        elif used[next_v]:
            flg = False
        # 見られていない場合、再帰的に探索
        else:
            dfs(G, next_v,v)

# 実行
cnt = 0
for i in range(N):
    if not used[i]:
        flg = True
        dfs(G,i,-1)
        cnt += flg 
print(cnt)