# 優先度付きqueueの導入
# http://n-knuu.hatenablog.jp/entry/2015/05/30/183718

import heapq
X,Y,Z,K = map(int,input().split())
As = sorted(list(map(int,input().split())),reverse=True)
Bs = sorted(list(map(int,input().split())),reverse=True)
Cs = sorted(list(map(int,input().split())),reverse=True)
q = []
heapq.heapify(q)
heapq.heappush(q,(-(As[0]+Bs[0]+Cs[0]),0,0,0))
list_ijk = [(0,0,0)]
for i in range(K):
    # valueのマイナス値の小さい順にpop(優先度付きqueue)
    v,i,j,k = heapq.heappop(q)
    if i < len(As)-1 and (i+1,j,k) not in list_ijk:
        heapq.heappush(q,(-(As[i+1]+Bs[j]+Cs[k]),i+1,j,k))
        list_ijk.append((i+1,j,k))
    if j < len(Bs)-1 and (i,j+1,k) not in list_ijk:
        heapq.heappush(q,(-(As[i]+Bs[j+1]+Cs[k]),i,j+1,k))
        list_ijk.append((i,j+1,k))
    if k < len(Cs)-1 and (i,j,k+1) not in list_ijk:
        heapq.heappush(q,(-(As[i]+Bs[j]+Cs[k+1]),i,j,k+1))
        list_ijk.append((i,j,k+1))
    print(-v)    
"""
# どうやって自明な条件で計算量を落としていくか
# 不等式に注目。pythonが耐えるのは10^6程度
X,Y,Z,K = map(int,input().split())
As = sorted(list(map(int,input().split())),reverse=True)
Bs = sorted(list(map(int,input().split())),reverse=True)
Cs = sorted(list(map(int,input().split())),reverse=True)

# ABでソート
AB = []
for A in As:
    for B in Bs:
        AB.append(A+B)
ABs = sorted(AB,reverse=True)

# その中からK番目まで
ABC = []
for i in range(min(len(ABs),K)):
    for C in Cs:
        ABC.append(ABs[i]+C)

ABCs = sorted(ABC,reverse=True)
for i in range(K):
    print(ABCs[i])
"""