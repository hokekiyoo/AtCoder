N = int(input())
Aij = []
for i in range(N):
    Aij.append([int(i) for i in input().split()])

dp = [[0]*3]*N

dp[0] = Aij[0]

for i in range(1,N):
    a,b,c = dp[i-1]
    ## 当日選んだところベースで、次のあれが決まる
    dp[i][0] = Aij[i][0] + max(b, c)
    dp[i][1] = Aij[i][1] + max(c, a)
    dp[i][2] = Aij[i][2] + max(a, b)

    ### このやり方はなにかまずい(中身が書き換わっている？)
    # dp[i][0] = Aij[i][0] + max(dp[i-1][1], dp[i-1][2])
    # dp[i][1] = Aij[i][1] + max(dp[i-1][2], dp[i-1][0])
    # dp[i][2] = Aij[i][2] + max(dp[i-1][0], dp[i-1][1])


print(max(dp[-1]))