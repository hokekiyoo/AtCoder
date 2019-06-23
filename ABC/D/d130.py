from itertools import accumulate
import bisect

N,K = map(int, input().split())
As = list(map(int, input().split()))
cum = list(accumulate(As))
ans = 0
for c in cum[::-1]:
    if c < K:
        continue
    d = c - K
    index= bisect.bisect_right(cum,d)
    ans += index+1
print(ans)