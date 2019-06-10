from itertools import accumulate
N = int(input())
Ws  = list(map(int, input().split()))
S = sum(Ws)
acc = list(accumulate(Ws))
ans = S
for i in range(N):
    ans = min(ans,abs(S-2*acc[i]))
print(ans)