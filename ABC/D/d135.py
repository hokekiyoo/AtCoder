S = input()
N = len(S)

mod = 10**9 +7
dp = [[0] * 13 for i in range(10**6)]

dp[0][0] = 1
for i,s in enumerate(S):
    keta = (N-i-1)%6
    if s != "?":
        for j in range(13):
            amari = (j + int(s)*10**keta)%13 #桁を追加
            dp[i+1][amari] += dp[i][j]
    else:
        for j in range(13):
            for k in range(10):
                amari = (j + k*10**keta)%13
                dp[i+1][amari] += dp[i][j]
    for j in range(13):
        dp[i+1][j] %= mod
print(dp[N][5]%mod)