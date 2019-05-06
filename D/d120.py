class UnionFind:
    def __init__(self, n):
        self.par = [-1 for i in range(n+1)]
        self.size = [1 for i in range(n+1)]
    # 検索
    def find(self, x):
        path = []
        curr = x
        # 親ノードの手前で止まる(どの根に紐づくかの情報を持ちながら)
        while self.par[curr] != -1:
            # 自分自身じゃない場合は、上にさかのぼって検索(再帰的に)
            path.append(curr)
            curr = self.par[curr]
        for p in path:
            self.par[p] = curr
        return curr

    # 結合
    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        self.par[y] = x
        self.size[x] += self.size[y]
        self.size[y] = 1

    # 判定
    def judge(self,x,y):
        return self.find(x) == self.find(y)

N, M = map(int,input().split())
pairs = [tuple(map(int,input().split())) for _ in range(M)]
uf = UnionFind(N)
p = N*(N-1)//2
ans = [p]
for a,b in reversed(pairs[1:]):
    if not uf.judge(a,b):
        size_a = uf.size[uf.find(a)]
        size_b = uf.size[uf.find(b)]
        uf.union(a,b)
        size_a_update = uf.size[uf.find(a)]
        p = p + size_a*(size_a-1)//2 + size_b*(size_b-1)//2 - size_a_update*(size_a_update-1)//2

    ans.append(p)
for a in reversed(ans):
    print(a)


"""
時間的にアレだったやつ
N, M = map(int,input().split())
pairs = [(a,b) for map(int,input().split) in range(M)]

connections = []
ans = [int(comb(N,2,exact=True))]
for Ai, Bi in pairs[::-1]:
    # connect_flg = False
    ind = []
    for i,connection in enumerate(connections):
        if Ai in connection and Bi in connection:
            ind = [0]
            continue
        elif Ai in connection:
            connections[i].append(Bi)
            # connect_flg = True
            ind.append(i)
        elif Bi in connection:
            connections[i].append(Ai)
            # connect_flg = True
            ind.append(i)
    # ２つをつなぐものは、一つにまとめる
    if len(ind) == 2:
        connections[ind[0]].extend(connections[ind[1]])
        connections[ind[0]] = list(set(connections[ind[0]]))
        connections.remove(connections[ind[1]])            
    elif len(ind) == 0:
        connections.append([Ai,Bi])
    # 不便度の計算
    cnt = int(comb(N,2,exact=True))
    # print(connections,cnt)
    for connection in connections:
        cnt -= int(comb(len(connection),2,exact=True))
    ans.append(cnt)
for a in ans[::-1][1:]:
    print(a)
"""