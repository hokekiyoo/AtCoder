"""
1 2 3 4 5 6 ... N
任意のiについて
iの倍数が書かれた箱に入っているボールの個数の和を2で割ったあまりがai
"""

N = int(input())
As = list(map(int, input().split()))

"""
1 2 3 4 5 6
0 1 0 1 0 1

i = 1  sum(As)%2 
i = 2  sum(As[::2]%2)

1    1 1 1 1 1 1 1 1 1 1
2    0 1 0 1 0 1 0 1 0 1
3    0 0 1 0 0 1 0 0 1 0
4    0 0 0 1 0 0 0 1 0 0
5    0 0 0 0 1 0 0 0 0 1
6    0 0 0 0 0 1 0 0 0 0
7    0 0 0 0 0 0 1 0 0 0
8    0 0 0 0 0 0 0 1 0 0 
9    0 0 0 0 0 0 0 0 1 0
10   0 0 0 0 0 0 0 0 0 1

後ろから決めていく？
"""
Bs = [0] * N
inball = []
for i in [N-i for i in range(N)]:
    n = N//i
    cnt = 0
    for j in [n-i for i in range(n)]:
        cnt += Bs[i*j-1]
    Bs[i-1] = (cnt+As[i-1]) % 2

ans = [i+1 for i,b in enumerate(Bs) if b==1]
M = len(ans)
print(M)
if M > 0:
    print(*ans)

