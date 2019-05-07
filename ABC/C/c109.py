# 最大公約数なきがするけど。
def gcd(n, m):
    # 最大公約数
    a = max(n,m)
    b = min(n,m)
    while b:
        a, b = b, a % b
    return a

N, X = map(int,input().split())
xs = [int(i) for i in input().split()]

xs.append(X)
xs = sorted(xs)
if len(xs) == 2:
    print(abs(xs[0]-xs[1]))
else:
    diffs = [xs[i]-xs[i-1] for i in range(1,len(xs))] #差を取る
    gcd_min = gcd(diffs[0],diffs[1])
    for i in range(2,len(diffs)):
        gcd_min = gcd(gcd_min, diffs[i])

    print(gcd_min)