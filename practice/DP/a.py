N = int(input())
hs = [int(i) for i in input().split()]
dp = [10000000] * N
for i,h in enumerate(hs):
    if i == 0:        
        # 0は初期化されている
        dp[i] = 0
        continue
    elif i == 1:
        # 1は1通りしか無い
        dp[i] = dp[i-1] + abs(hs[i-1]-h)
    else:
        # 1個前か2個前で、コストが最小になるやつ
        dp[i] = min(dp[i-1]+abs(hs[i-1]-h),dp[i-2]+abs(hs[i-2]-h))
# print(dp)
print(dp[-1])