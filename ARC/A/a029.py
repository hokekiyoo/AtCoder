N = int(input())
ts = []
for i in range(N):
    ts.append(int(input()))
# バイナリ化
t_min = 1000000
for n in range(2**N):
    nstr = "{:010b}".format(n)
    bs = list(nstr[-N:])
    times = [0,0]
    for t, b in zip(ts,bs):
        times[int(b)] += t
    t_min = min(t_min,max(times))
print(t_min)

"""
この問題はすべてのお肉の焼き時間の合計値をMとおいたときに、
M/2以上で最小の部分和を求める問題に帰着できる。(らしい)
そうすると、動的計画法でO(2^N)->O(NM) 
参考 : https://qiita.com/drken/items/a5e6fe22863b7992efdb
"""