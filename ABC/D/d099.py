N,C = map(int, input().split())
Dij = []
for i in range(C):
    Dij.append(list(map(int, input().split())))
cij = []
for i in range(N):
    cij.append(list(map(int, input().split())))
# 同じ色にしたいグリッドのまとめ
C1 = []
C2 = []
C3 = []
for i in range(N):
    for j in range(N):
        if (i+j)%3 == 0:
            C1.append(cij[i][j])
        if (i+j)%3 == 1:
            C2.append(cij[i][j])
        if (i+j)%3 == 2:
            C3.append(cij[i][j])

"""
3色で塗る
"""
cost_c1 = []
cost_c2 = []
cost_c3 = []
for Y in range(C):
    #1
    cost = 0
    for X in C1:
        cost += Dij[X-1][Y]
        # print(X-1,"->",Y,":",Dij[X-1][Y])
    cost_c1.append(cost)
    #2
    cost = 0
    for X in C2:
        cost += Dij[X-1][Y]
        # print(X-1,"->",Y,":",Dij[X-1][Y])
    cost_c2.append(cost)
    #3
    cost = 0
    for X in C3:
        cost += Dij[X-1][Y]
        # print(X-1,"->",Y,":",Dij[X-1][Y])    
    cost_c3.append(cost)

#1->2->3

minA = 0

ans = float("inf")
for i,c1 in enumerate(cost_c1):
    for j,c2 in enumerate(cost_c2):
        for k,c3 in enumerate(cost_c3):
            if i!=j and j!=k and k!=i:
                ans = min(ans,c1+c2+c3) 
print(ans)