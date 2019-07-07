N,M = map(int, input().split())
xs,ys,zs = [], [], []
"""
sum000 +++
sum001 ++-
sum010 +-+
sum011 +--
sum100 -++
sum101 -+-
sum110 --+
sum111 ---
"""


sum000, sum001, sum010,sum011 = [], [], [], []
sum100, sum101, sum110,sum111 = [], [], [], []
sums = [[] for i in range(8)]
for i in range(N):
    x,y,z = map(int, input().split())
    sums[0].append(x+y+z)
    sums[1].append(x+y-z)
    sums[2].append(x-y+z)
    sums[3].append(x-y-z)
    sums[4].append(-x+y+z)
    sums[5].append(-x+y-z)
    sums[6].append(-x-y+z)
    sums[7].append(-x-y-z)

ans = 0
for s in sums:
    s1 = sorted(s,reverse=False)
    s2 = sorted(s,reverse=False)
    x = max(abs(sum(s1[:M])),abs(sum(s2[:M])))
    ans = max(ans,x)
print(ans)