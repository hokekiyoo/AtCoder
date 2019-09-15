from bisect import bisect_right
from collections import defaultdict

S = input()
S_set = set(S)
d = defaultdict(list)
for i,s in enumerate(S):
    d[s].append(i)
# print(d)

T = input()
T_set = set(T)
for t in T_set:
    if t not in S_set:
        print(-1)
        exit()

cnt = 0
loop = 0
prev = -1

for t in T:
    num = d[t]
    a = bisect_right(num,prev)
    print(prev,a,num)
    
    if a >= len(num):
        loop += 1
        a = 0
    prev = num[a]

print(prev+1+(loop)*len(S))