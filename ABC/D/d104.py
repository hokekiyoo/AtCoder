"""
保存する量
dp[i][j]
i番目の文字で、ABCのうちどこまでいっていて、
そのとき残りの方法の個数

0 まだ何も選んでいない
1 Aだけ選んでいる
2 A,Bまで選べている
"""


S = input()
dp = [[0]*3 for i in range(lens(S)+1)]
for i,s in enumerate(S):
    for j in range(3):
        if i == N:
            dp[i][j] =
         
        dp[i+1][j] = 
