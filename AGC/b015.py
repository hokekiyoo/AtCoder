S = list(input())
n = len(S)

"""
# 通常時 : 
Uならそれ以上の階は1回でいける
Dならそれ以下の回は1回でいける
それ以外は、2回かかる
"""
cnt = 0
u_cnt = 0
for i,s in enumerate(S):
    if s == "U":
        cnt += (n-i-1)
S.reverse()
for i,s in enumerate(S):
    if s == "D":
        cnt += (n-i-1)

N = n*(n-1)
ans = cnt + 2*(N-cnt)
print(ans)