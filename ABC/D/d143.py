N = int(input())
Ls = sorted(list(map(int, input().split())),reverse=True) #ソートしておく
r = list(reversed(Ls))
from bisect import bisect_right
ans = 0
for i in range(N):
    for j in range(i+1,N):
        x = Ls[i] - Ls[j]
        ind = bisect_right(r,x)
        ans += max(0,N-ind-j-1)
print(ans)