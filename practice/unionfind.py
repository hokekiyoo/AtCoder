# unionfind木構造
# unionfindについてはここhttps://www.slideshare.net/chokudai/union-find-49066733
# グループに属するかの判定(find)や、グループ結合(union)に強い
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
        # # ランクが低い木の根を高い木の根にくっつける
        # if self.rank[x] < self.rank[y]:
        #     self.par[x] = y
        # else:
        #     self.par[y] = x
        # if self.rank[x] == self.rank[y]:
        #     self.rank[x] += 1
        self.par[x] = y
    
    # 判定
    def judge(self,x,y):
        return self.find(x) == self.find(y)

if __name__ == "__main__":
    # unionfindを試す
    vs = [[1,2],[3,4],[5,6],[1,3]]
    uf = UnionFind(10)
    for x,y in vs:
        if not uf.judge(x,y):
            print("unit",x,y)
            uf.union(x,y)
            # uf.find(x)
            # uf.find(y)
    # 根っこを見つける
    for i in range(1,7):
        print(uf.find(i))
