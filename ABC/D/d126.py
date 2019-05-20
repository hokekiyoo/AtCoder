from collections import deque

### グラフの構造:2D配列
## G[u] = (v, l) 接続する頂点と、そこに到達するまでの辺の長さ(コスト)

N = int(input())
G = [[] for i in range(N)]
for i in range(N-1):
    u,v,w = map(int,input().split())
    # グラフに頂点と距離を追加
    G[u-1].append((v-1,w))
    G[v-1].append((u-1,w))


# グラフのBFSなやり方？
# どこか1点を選んで、頂点を全探索
used = [0] * N
que = deque([0])
ans = [False] * N
while que:
    # print(list(que))
    u = que.popleft()
    for v,w in G[u]:
        if used[v]:
            # すでにチェックされていたら無視
            continue
        else:
            # wが奇数⇨色を分ける
            # wが偶数⇨色をそのまま
            if w%2 == 0:
                ans[v] = ans[u]
            else:
                ans[v] = not ans[u]
            # print(w,ans[u],ans[v])
            que.append(v)
            used[u] = True
for a in ans:
    print(int(a))