# import numpy as np
"""
タイムアウトする
"""
N,W = map(int, input().split())

INF = 10**10
vsum = 1000*N
dp = [INF for i in range(vsum+1)]
dp[0] = 0


for _ in range(N):
    w,v = map(int,input().split())
    dp1 = [d for d in dp]
    for i,d in enumerate(dp):
        if d == INF:
            continue
        else:
            if i + v <= vsum:
                dp[i+v] = min(dp1[i+v], dp1[i]+w)
    
ans = 0
for i,d in enumerate(dp):
    if d <= W:
        ans = i
print(ans)


"""
タイムアウトしない
"""
import numpy as np
N,W = map(int, input().split())
INF =  10**10
V_max = 100001
N_max = 101
dp = np.ones(V_max,dtype=np.int64)*INF
dp[0] = 0
for i in range(N):
    a = np.ones(V_max)*INF
    w,v = map(int,input().split())
    # np.minimum(dp[i][:-v]+w,dp[i][v:],out=dp[i+1][v:])
    np.minimum(dp[:-v]+w,dp[v:],out=dp[v:])
ans = 0
for i,d in enumerate(dp):
    if d<=W:
        ans = i
print(ans)