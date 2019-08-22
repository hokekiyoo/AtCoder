"""
WEEWW
<>><<
01100
10100
01000
10000
10010

下記の和
1. リーダーより左にいるWの数
2. リーダーより右にいるEの数
"""

N = int(input())
S = input()
# 1.
cntW = 0
W_num = [0]*N
for i,s in enumerate(S):
    if s == "W":
        cntW += 1
    W_num[i] = cntW
        
# 2. 
cntE = 0
E_num = [0]*N
for i,s in enumerate(S[::-1]):
    if s == "E":
        cntE +=1 
    E_num[i] = cntE
E_num = E_num[::-1]

ans = 10**10
for e,w in zip(E_num, W_num):
    cnt = e + w - 1
    ans = min(cnt, ans)
print(ans)