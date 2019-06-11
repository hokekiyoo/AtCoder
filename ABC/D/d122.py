"""
1.4種類の文字ATGC
2.AGCを作ってはならない
3.隣り合う文字を1箇所だけ入れ替えても、AGCになってはならない

3. が厄介
変えないAGC 
0-1 A*GC
1-2 GAC
2-3 ACG
3-4 AG*C

とりあえず3文字分テーブルに持たせながらdp？
"""

mod = 10**9 + 7
N = int(input())
dp =[[[[0]*5 for i in range(5)] for j in range(5)] for n in range(108)]

nul = 0
A = 1
G = 2
C = 3
T = 4

"""
AGC
0-1 A*GC
1-2 GAC
2-3 ACG
3-4 AG*C
"""
dp[0][0][0][0] = 1
for n in range(N):
    for n3 in range(5):             # 3つ前
        for n2 in range(5):         # 2つ前
            for n1 in range(5):     # 1つ前
                for s in range(1,5): # 今
                    if n2 == A and n1 == G and s == C: continue
                    if n3 == A and n1 == G and s == C: continue
                    if n2 == G and n1 == A and s == C: continue
                    if n2 == A and n1 == C and s == G: continue
                    if n3 == A and n2 == G and s == C: continue
                    # print(n,n1,n2,n3,s)
                    dp[n+1][n2][n1][s] += dp[n][n3][n2][n1]                    
ans = 0
for i in range(5):
    for j in range(5):
        for k in range(5):
            ans += dp[N][i][j][k]
print(ans%mod)