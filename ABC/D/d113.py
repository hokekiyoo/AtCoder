# あみだくじ
H, W, K = map(int,input().split())
# h番目のときに、k本目にたどりつく通り
dp = [[0 for j in range(W)] for i in range(H+1)] #高さHでK本
# dp[h][k] = dp[h-1][k-1]*(hにおけるk-1からkへの線の引き方) 
#          + dp[h-1][k]*(hにおける、k-1,k+1から線がひかれないとき) 
#          + dp[h-1][k*1]*(hにおけるk+1からkへの線の引き方)
# 線の引き方は、対象の線からフィボナッチ的に増えていく。
# なぜならx(引かない)の数だけ隣の候補が増える

def fib(n):
    fibonacci = [1,1,2,3,5,8,13,21,34]
    return fibonacci[n]

if W == 1:
    print(1)
else:

    dp[0][0] = 1
    for h in range(1,H+1):
        for k in range(W):
            if 0 < k < W-1: 
                num1 = dp[h-1][k-1]*fib(W-k-1)*fib(k-1)
                num2 = dp[h-1][k]  *fib(W-k-1)*fib(k)
                num3 = dp[h-1][k+1]*fib(W-k-2)*fib(k)
            if k == 0: 
                num1 = 0
                num2 = dp[h-1][k]  *fib(W-k-1)*fib(k)
                num3 = dp[h-1][k+1]*fib(W-k-2)*fib(k)
                
            if k == W-1: 
                num1 = dp[h-1][k-1]*fib(W-k-1)*fib(k-1)
                num2 = dp[h-1][k]  *fib(W-k-1)*fib(k)
                num3 = 0
            # print("({},{}):{}+{}+{}".format(h,k,num1,num2,num3))
            dp[h][k] = num1+num2+num3
    mod = 10**9+7
    print(dp[-1][K-1]%mod)

