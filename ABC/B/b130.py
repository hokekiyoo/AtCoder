from itertools import accumulate
N,X = map(int, input().split())
Ls = [0]+list(map(int, input().split()))
D = list(accumulate(Ls))

flg = False
for i,d in enumerate(D):
    if d>X:
        flg = True
        break
if flg:
    print(i)
else:
    print(i+1)