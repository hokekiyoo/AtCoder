# 部分文字列 : 末尾と先頭からいくらか削っても残る文字列
# abc -> a,b,c,ab,bc,abc acはちがう
# 範囲が決まっているのは累積和がバシッとはまることが多い。とくに複数回の参照とか
N, Q = map(int,input().split())
S = input()

accum = [0]
cnt = 0
for i in range(1,N):
    if S[i-1:i+1] == "AC":
        cnt += 1
    accum.append(cnt)
print(accum)

for i in range(Q):
    l,r = map(int, input().split())
    print(accum[r-1]-accum[l-1])