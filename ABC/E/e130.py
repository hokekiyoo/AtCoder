"""
適当に実験してdpやったやつ。
あんまり根拠が無いので微妙。
"""
# N,M = map(int, input().split())
# Ss = list(map(int, input().split()))
# Ts = list(map(int, input().split()))
# mod = 10**9 + 7
# x = 2160
# dp = [[0]*x for i in range(x)]
# for i in range(N):
#     for j in range(M):
#         if Ss[i] == Ts[j]:
#             dp[i+1][j+1] = (dp[i][j+1] + dp[i+1][j] + 1) % mod
#         else:
#             dp[i+1][j+1] = (dp[i][j+1] + dp[i+1][j] - dp[i][j])%mod
"""
N^2とか、NMとかの計算量を持つときは、
二次元的に調べてみるというmethodが良いのではないか。

E，common sequence の末尾が i, j であるものが dp[i][j] に入っていて，
新たに S[i]==T[j] なる点が存在するたびにそこまでの二次元累積和に追加していく

sum[i][j] : S[i] == T[j] を既存の common sequence の末尾に追加する
1 : 末尾単体で common sequence を開始するか
"""
N,M = map(int, input().split())
Ss = list(map(int, input().split()))
Ts = list(map(int, input().split()))
mod = 10**9 + 7

x = 2160
dp = [[0]*x for i in range(x)]
sum2d = [[0]*x for i in range(x)]
for i in range(N):
    for j in range(M):
        if Ss[i] == Ts[j]:
            dp[i+1][j+1] = sum2d[i][j] + 1
        sum2d[i+1][j+1] = (dp[i+1][j+1]+sum2d[i][j+1]+sum2d[i+1][j]-sum2d[i][j])%mod
print((sum2d[N][M]+1)%mod)