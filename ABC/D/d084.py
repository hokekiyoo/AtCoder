Q = int(input())


# 約数
def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)
    return divisors
N = 5*10**4
acc = [0]*(N+1)
cnt = 0
for i in range(N+1):
    n1 = 2*i + 1
    n2 = i+1
    div1 = make_divisors(n1)
    div2 = make_divisors(n2)    
    if len(div1) == len(div2) == 2:
        cnt += 1
    acc[i] = cnt
# print(acc[:10])
for i in range(Q):
    l_,r_ = map(int, input().split())
    l = (l_-1)//2
    r = (r_-1)//2
    if l > 0:
        print(acc[r]-acc[l-1])
    else:
        print(acc[r])


def getprime(n):
    if not isinstance(n, int):
        raise TypeError("Input int")
    if n < 2:
        raise ValueError("N >= 2")
    prime = []
    # 約数はsqrt(N)まで調べればOK
    data = [i+1 for i in range(1,n)]
    while True:
        p = data[0]
        if p >= int(n**0.5):
            return prime+data
        prime.append(p)
        # pで割り切れないものだけを残す
        data = [d for d in data if d%p != 0]

