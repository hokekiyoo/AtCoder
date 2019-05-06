N, K = map(int,input().split())
hs = [int(i) for i in input().split()]

dp = [1000000]*N
dp[0] = 0
for i in range(1,N):
    x = max(0, i-K)
    # dp[i] = min(dp[i], dp[min_ind]+abs(hs[min_ind]-hs[i]))
    # 一気に見てからminを求める
    dp[i] = min([dpj + abs(hs[i] - hj) for hj, dpj in zip(hs[x:i], dp[x:i])])
# print(dp)
print(dp[-1])