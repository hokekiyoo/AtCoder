N,K = map(int, input().split())
As = list(map(int, input().split()))


# if K % 2 == 1:
#     K = 1
# else:
#     K = 2
n = len(set(As))
K %= n
X = [As[i%N] for i in range(N*K)]

s = []
Nmax = 2*10**5 + 1
dp = [0] * Nmax #最初に入ってあるiの数

set_x = set()
for i,x in enumerate(X):
    seq = dp[x]
    if seq == 0:
        dp[x] = i+1
        set_x.add(x)    
    else:
        set_tmp = set_x.copy()
        for s in set_tmp:
            if seq - dp[s] <= 0:
                dp[s] = 0
                set_x.remove(s)

ans1 = sorted([(dp[s],s) for s in set_x])
ans = [i for x,i in ans1]
print(*ans)