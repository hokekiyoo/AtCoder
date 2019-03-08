"""
1回目
"""
# import numpy as np
# N, M = map(int,input().split())
# Ps = [[] for _ in range(N)]
# for i in range(M):
#     j, Y = map(int,input().split())n
#     Ps[j-1].append([i,Y])

# rets = [""]*M
# for i_city,P in enumerate(Ps):
#     if len(P)==0:
#         continue
    
#     inds = np.array(P)[:,0]
#     years = np.array(P)[:,1]
#     sorts = np.argsort(years)
    
#     ## 降順/昇順に手こずりすぎ
#     for i,(ind,s) in enumerate(zip(inds,sorts)):
#         a = np.where(sorts==i)[0][0]
#         rets[ind] = "{:06d}{:06d}".format(i_city+1,a+1)
# for ret in rets:
#     print(ret)

"""
2回目
"""
# N,M = 2,4
# s = [[2,55],[2,77],[2,33],[1,44]]
# Ps = np.array(s)

# import numpy as np
# N, M = map(int,input().split())
# Ps = np.zeros((M,2))
# for i in range(M):
#     j, Y = map(int,input().split())
#     Ps[i] = [j,Y]

# def rank(argsort):
#     x = np.zeros(len(argsort))
#     for i,s in enumerate(argsort):
#         x[s] = i+1
#     return list(x)


# ranks = []
# for i in range(N):
#     s = np.argsort(Ps[np.where(Ps[:,0]==i+1)][:,1])
#     ranks.append(rank(s))

# for index, year in Ps:
#     index = int(index)
#     print("{:06d}{:06d}".format(index,int(ranks[index-1][0])))
#     ranks[index-1].pop(0)

"""
3回目
"""
import numpy as np
from bisect import bisect_left

# N,M = 2,4
# s = [[2,55],[2,77],[2,33],[1,44]]
# Ps = np.array(s)

N, M = map(int,input().split())
Ps = np.zeros((M,2))
for i in range(M):
    j, Y = map(int,input().split())
    Ps[i] = [j,Y]

dist = []
for i in range(N):
    s = Ps[np.where(Ps[:,0]==i+1)][:,1]
    dist.append(np.sort(s))

for city, year in Ps:
    city = int(city)
    rank = bisect_left(dist[city-1],year)
    print("{:06d}{:06d}".format(city,rank+1))

"""
模範解答
"""
from collections import defaultdict
from bisect import bisect_left
N, M = map(int, input().split())
A = []
B = defaultdict(list)
 
for i in range(M):
    p, y = map(int, input().split())
    A.append([p, y])
    B[p].append(y)
 
for key in B.keys():
    B[key].sort()

# print(A,B)
# for a in A:
#     print(a[0],a[1],B[a[0]],bisect_left(B[a[0]],a[1]))
for a in A:
    print("%06d%06d" % (a[0], bisect_left(B[a[0]], a[1])+1))