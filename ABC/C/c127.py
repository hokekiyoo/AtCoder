N, M = map(int,input().split())
"""
提出した回
"""
#Ls,Rs = [],[]
# for i in range(M):
#     L,R = map(int,input().split())
#     Ls.append(L)
#     Rs.append(R)

# print(max(0,min(Rs)-max(Ls)+1))

"""
imos
"""
from itertools import accumulate
imos = [0]*(N+1)
for i in range(M):
    L,R = map(int,input().split())
    imos[L] += 1
    imos[R+1] -= 1
acc = list(accumulate(imos))
print(sum([1 for a in acc if a == M]))