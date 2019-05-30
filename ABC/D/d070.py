from collections import deque

N = int(input())
G = [[] for i in range(N)]
for i in range(N-1):
    u,v,w = map(int,input().split())
    # グラフに頂点と距離を追加
    G[u-1].append((v-1,w))
    G[v-1].append((u-1,w))


Q, K = map(int,input().split())
dist_from_K = [0]*N
used = [False] * N
used[K-1] = True
before = K-1

q = deque([K-1])
while len(q) > 0:
    a = q.popleft()
    Vs = G[a]
    for u, w in Vs:
        if not used[u]:
            q.append(u)
            dist_from_K[u] = dist_from_K[a] + w
            used[u] = True

ans = []
for _ in range(Q):
    x,y = map(int,input().split())
    ans.append(dist_from_K[x-1]+dist_from_K[y-1])
for a in ans:
    print(a)