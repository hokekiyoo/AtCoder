N,M,L = map(int, input().split())
Edges = [map(int, input().split()) for i in range(M)]
Q = int(input())
Queries = [map(int, input().split()) for i in range(Q)]

INF = 10**18
# 初期化
d = [[INF]*N for i in range(N)]
for i in range(N):
    d[i][i] = 0
for a,b,c in Edges:
    a -= 1
    b -= 1
    # 多重辺の場合はMIN
    d[a][b] = c
    d[b][a] = c
# 最適化(わーしゃゆふよいど)
for k in range(N):
    for i in range(N):
        # 左右は対称だろう
        for j in range(i+1,N):
            d[i][j] = min(d[i][j], d[i][k] + d[k][j])
            d[j][i] = d[i][j]

# 初期化2
d2 = [[INF]*N for i in range(N)]
for i in range(N):
    d2[i][i] = 0
for i in range(N):
    for j in range(N):
        # 給油できるところに辺を張る
        if d[i][j] <= L:
            d2[i][j] = 1
for k in range(N):
    for i in range(N):
        for j in range(i+1,N):
            d2[i][j] = min(d2[i][j], d2[i][k] + d2[k][j])
            d2[j][i] = d2[i][j]
            

#query
for a,b in Queries:
    s = min(a,b)-1
    t = max(a,b)-1
    
    ans = d2[s][t]
    if ans == INF:
        ans = 0
    print(ans-1)