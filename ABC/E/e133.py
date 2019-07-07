import sys
sys.setrecursionlimit(100000)

from collections import deque
# 木構造を作る
N,K = map(int, input().split())
G = [[] for i in range(N)]
for i in range(N-1):
    # グラフに頂点を追加(距離があるときは,u,vの後に入れる)
    u,v = map(int,input().split())
    G[u-1].append((v-1))
    G[v-1].append((u-1))

start = 0

used = [False] * N
used[start] = True
mod = 10**9 + 7
cnt = 0
ans = K
def dfs(G, i, v):
    global cnt
    global ans 
    #グラフ中の次のVについて
    used[v] = True
    cnt += 1
    numv = 0
    for next_v in G[v]:
        # すでに見られていたら無視
        if used[next_v]: continue
        numv += 1
        ans %= mod
        if i <= 1:
            ans *= K-i-numv
        else:
            ans *= K - 1 - numv
        # print("v",v,"n{},cnt{},ans{}".format(numv,cnt,ans))
        ans %= mod
        dfs(G,i+1, next_v)



dfs(G,0,start)
print(ans%mod)
