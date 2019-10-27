
"""
bitDPというらしい
dp[i][j] = i番目の入力に対して、状態jを実現する最小値
j : 2^12通り。それぞれの宝箱をbitと見立てる
"""

N, M = map(int, input().split())
INF = 10**5+1

dp = [INF for i in range(2**N+1)]
dp[0] = 0

for i in range(M):
    cost,b = map(int, input().split())
    boxes = list(map(int, input().split()))
    status = 0
    for box in boxes:
        status += 2**(box-1)
    for j in range(2**N):
        if dp[j] != INF:
            nxt = status | j
            dp[nxt] = min(dp[j] + cost, dp[nxt])

ans = dp[2**N-1]
if ans == INF:
    print(-1)
else:
    print(ans)
