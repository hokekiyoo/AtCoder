# 素因数分解
N = int(input())
ans = 0
s = 0
for i in range(1,N+1,2):
    L = i
    divisors=[0]*(i+1)
    cnt = 1
    # 素因数分解
    for j in range(2,N+1):
        while True:
            if L % j == 0:
                divisors[j] += 1
                L //= j
                if L == 1:
                    s = 1 #1はこれ以上素因数を産まない
                    break
            else:
                break

    for div in divisors:
        cnt *= (div+1)
    if cnt == 8:
        ans += 1
    # print(i,cnt,ans,divisors)

print(ans)