N = int(input())
xs = [1]
i = 1
while N >= 6**i:
    if 9**i <= N:
        xs.append(9**i)
    xs.append(6**i)
    i += 1
X = sorted(xs)
# print(X)

# N円のときの最小回数
dp = [10000000000] * 1008000
dp[0] = 0
for i in range(N):
    for x in X:
        dp[i+x] = min(dp[i]+1, dp[i+x])
print(dp[N])