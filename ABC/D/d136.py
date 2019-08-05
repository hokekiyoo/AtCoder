"""
保存量を考える。パリティ(偶奇)が保存
1回ずつの操作なので、進んだ距離=時間
十分時間が経っても
奇数上にあるものと、偶数上にあるものが保存される

RRRLL   odd even
11111   3   2
01220   2   3
00320   3   2
00230   2   3
"""

S = input()
# S = "RL"
rs = []
ls = []
inds = []

s_inv = S[::-1]
rcnt = 0
#Rを数える
for i,s in enumerate(S):
    if s == "R":
        rcnt += 1
    else:
        if rcnt > 0:
            #記録
            rs.append(rcnt)
            inds.append(i-1)
        rcnt = 0
#Lを数える
# print(s_inv)
lcnt = 0
for i,s in enumerate(s_inv):
    if s == "L":
        lcnt += 1
    else:
        if lcnt > 0:
            ls.append(lcnt)
        lcnt = 0
ls = ls[::-1]

ans = [0]*len(S)
for i,r,l in zip(inds,rs,ls):
    adds = r+l
    # print(adds,i)
    if (r+l)%2 == 0:
        ans[i] = (r+l)//2
        ans[i+1] = (r+l)//2
    else:
        if r%2 == 1:
            ans[i] = (r+l)//2 + 1
            ans[i+1] = (r+l)//2 
        else:
            ans[i] = (r+l)//2
            ans[i+1] = (r+l)//2 + 1

print(*ans)