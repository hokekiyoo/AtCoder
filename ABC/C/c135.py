N = int(input())
As = list(map(int, input().split()))
Bs = list(map(int, input().split()))

ans = 0
tmp = 0
for a,b in zip(As,Bs[:N]):
    # 前の余力で敵を頃す
    if tmp > 0:
        if a >= tmp:
            ans += tmp
            a -= tmp
        else:
            ans += a
            a = 0
    # 町から敵を頃す
    if a >= b:
        ans += b
        tmp = 0
    else:
        ans += a
        tmp = b-a
# 最後の町
a = As[N]
if a >= tmp:
    ans += tmp
else:
    ans += a

print(ans)