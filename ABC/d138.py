
N,Q  = map(int, input().split())

# 木
G = [[] for i in range(N)]
for i in range(N-1):
    u,v = map(int,input().split())
    G[u-1].append((v-1))
    G[v-1].append((u-1))

## クエリを覚えておく
scores = [0]*N
for i in range(Q):
    p,x = map(int, input().split())
    scores[p-1] += x 

# 和をとっていく
ans = [0]*N
ans[0] = scores[0]
used = [False] * N

"""
dfs TLEする。なんで
"""
# import sys
# sys.setrecursionlimit(100000)
# def dfs(G, v):
#    # vを訪問済みにする
#    used[v] = True
#    #グラフ中の次のVについて
#    for next_v in G[v]:
#        if used[next_v]: continue
#        ans[next_v] = ans[v] + scores[next_v]
#        dfs(G, next_v)
# dfs(G,0)
# print(*ans)

# 木をBFSをする
from collections import deque
used = [False] * N
used[0] = True # 始めどこから行くか
q = deque([0])
while len(q) > 0:
    v = q.popleft()
    Vs = G[v]
    for next_v in Vs: 
        if not used[next_v]:
            q.append(next_v)
            ans[next_v] = ans[v] + scores[next_v]
            used[next_v] = True
print(*ans)