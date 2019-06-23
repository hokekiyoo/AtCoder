a,b,c,d = map(int, input().split())

def gcd(n, m):
    # 最大公約数
    a = max(n,m)
    b = min(n,m)
    while b:
        a, b = b, a % b
    return a


def num(l,r,n):
    nr = r//n
    nl = l//n
    if l%n == 0:
        return nr-nl+1
    else:
        return nr-nl

LCM = int(c*d/(gcd(c,d)))
n = b-a+1
n1 = num(a,b,c)
n2 = num(a,b,d)
n3 = num(a,b,LCM)
print(n-(n1+n2-n3))
