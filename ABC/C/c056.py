"""
カンガルー
時刻iで長さiのジャンプをするx-i,x,x+i
0からスタートして、座標Xにつくまでの時間
"""

X = int(input())
# 大体のやつ
n = int((2*X)**0.5)+1
S = n*(n+1)//2

if S-X >= n:
    print(n-1)
else:
    print(n)