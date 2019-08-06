
"""
方針
ペアになっているものは、順序が任意になるという認識
-> UnionFindで行ける
"""

class UnionFind:
    def __init__(self, n):
        self.par = [i for i in range(n+1)]
        self.rank = [0 for i in range(n+1)]
    
    # 検索
    def find(self, x):
        if self.par[x] == x:
            return x
        else:
            # 自分自身じゃない場合は、上にさかのぼって検索(再帰的に)
            self.par[x] = self.find(self.par[x]) #根を置き換えていく
            return self.par[x]

    # 結合
    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        self.par[x] = y
    
    # 判定
    def judge(self,x,y):
        return self.find(x) == self.find(y)

n, m = map(int, input().split())
ps = list(map(int, input().split()))
uf = UnionFind(n)

for i in range(m):
    x,y = map(int, input().split())
    x -= 1
    y -= 1
    if not uf.judge(x,y):
        uf.union(x,y)
ans = 0
for i,p in enumerate(ps):
    if uf.find(p-1) == uf.find(i):
        ans += 1
print(ans)
