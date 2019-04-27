N  = int(input())
As = [int(i) for i in input().split()]

# 約数
def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)
    return divisors

# 最大公約数
def gcd(n, m):
    # 最大公約数
    a = max(n,m)
    b = min(n,m)
    while b:
        a, b = b, a % b
    return a

As = sorted(As)[::-1]
devs = make_divisors(gcd(As[0],As[1]))
if N > 2:
    devs.extend(make_divisors(gcd(As[1],As[2])))
    devs.extend(make_divisors(gcd(As[2],As[0])))
devs = list(set(devs))
cnt = 1
for dev in sorted(devs)[::-1]:
    a = sum([a%dev==0 for a in As])
    if N - a == 0 or N -a == 1:
        print(dev)
        break