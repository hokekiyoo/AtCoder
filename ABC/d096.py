"""
n%5 == 1 の素数を列挙する。
余りが同じなので、その5つの和は、どれをとっても
sum(5a+1,5b+1,...,5e+1)
= 5(a+b+c+d+e+1)
と、5の倍数(合成数)となる
"""

# 約数
def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)
    return divisors

cnt = 0
i = 0
primes = []
while cnt < 55:
    n = i*5 + 2
    if len(make_divisors(n)) == 2:
        primes.append(n)
        cnt += 1
    i += 1

N = int(input())
print(*primes[:N])