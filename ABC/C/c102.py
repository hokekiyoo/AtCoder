N, K = map(int,input().split())
# N以下の正の整数
# Kの倍数
# a+b, b+c, c+a a < b < c
# a, b, c すべてのmodが n*K/2 (n=1,2,3,...) となる必要がある
# a+b+c < 3N なので、int

# while n*K/2 > 3*N:
    # a = l*K + n*K/2 これが何通りあるか
# Kで割った余りが0 or K/2(偶数の時)以外ムリでは？
# Kで割った余りが0の時
ans = 0
cnt = N//K
ans += cnt ** 3
# Kで割った余りがK/2の時(偶数のみ)
if K % 2 == 0:
    n = 0
    cnt = 0
    while (n + 1/2) * K <= N:
        cnt += 1
        n += 1
    ans += cnt ** 3
print(ans)