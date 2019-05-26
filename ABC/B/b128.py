N = int(input())
from collections import defaultdict
res = defaultdict(list)
for i in range(N):
    S1,P1 = input().split()
    res[S1].append([P1,i])

for k,v in sorted(res.items()):
    lists = sorted(res[k])
    # print(lists)
    for l in lists:
        print(l[1])