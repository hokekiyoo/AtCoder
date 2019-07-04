from collections import deque
# 木構造を作る
N,M = map(int, input().split())

G = [[] for i in range(3*N)]
for i in range(M):
    # グラフに頂点を追加(距離があるときは,u,vの後に入れる)
    u,v = map(int,input().split())
    G[3*(u-1)].append((3*(v-1)+1))
    G[3*(u-1)+1].append((3*(v-1)+2))
    G[3*(u-1)+2].append((3*(v-1)))

S,T = map(int, input().split())

# 木をBFSをする
dist = [-1] * (3*N)
dist[3*(S-1)] = 0
q = deque([3*(S-1)])
while q:
    v = q.popleft()
    d = dist[v]
    Vs = G[v]
    for u in Vs:
        if dist[u] == -1:
            q.append(u)
            dist[u] = d + 1

ans = dist[3*(T-1)]
print(-1 if ans == -1 else ans//3)
