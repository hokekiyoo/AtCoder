from collections import deque

N = int(input())
nmax = 2*10**5
nhalf = 10**5

G = [[] for i in range(nmax)]
for i in range(N):
    x,y = map(int,input().split())
    G[x-1].append(nhalf+y-1)
    G[nhalf+y-1].append(x-1)

used = [False] * nmax
ans = 0
# 全探索
for i in range(nhalf):
    # 見つかったノードからBFS
    if G[i] != [] and not used[i]:
        cnt_1 = 0  #前半の連結
        cnt_2 = 0  #後半の連結
        q = deque([i])
        used[i] = True # 始めどこから行くか
        while len(q) > 0:
            a = q.popleft()
            if a < nhalf:
                cnt_2 += 1
            else:
                cnt_1 += 1
            Vs = G[a]
            for u in Vs: # 頂点以外の要素がグラフにあるときはここ
                if not used[u]:
                    q.append(u)
                    # なにか処理を書きたいときはここに書く
                    used[u] = True
        ans += cnt_1*cnt_2
print(ans-N)