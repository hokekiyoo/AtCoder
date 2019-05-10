from math import factorial
N, M = map(int,input().split())

# 素因数分解(小さい方から順に割っていく。sqrt(2)まで)
def factorize(n):
    i = 2
    table = [0]
    cnt= [0]
    while i * i <= n:
        while n % i == 0:
            n /= i
            if table[-1] != i:
                table.append(i)
                cnt.append(0)
            cnt[-1] += 1
        i += 1
    if n > 1:
        table.append(n)
        cnt.append(1)
    return table,cnt

# 組み合わせ
# 使わない。3つもfactorialする必要ないよね。
def combination(N,M):
    return factorial(N)//(factorial(M)*factorial(N-M))

fs,ns = factorize(M)

ans = 1
for n in ns[1:]:
    a = 1
    #　nCb = nPn-b/b!
    for i in range(N,n+N):
        a *= i
    ans *= a//factorial(n)
print(ans%(10**9+7))


"""
# 遅い。おそすぎる
from collections import deque

N, M = map(int,input().split())

# 約数
def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)
    return sorted(divisors,reverse=True)

# 重複順列
def count(nlist):
    nset = list(set(nlist))
    denom = 1
    for n in nset:
        cnt = nlist.count(n)
        prod = 1
        for i in range(1,cnt+1):
            prod *= i
        denom *= prod
    anom = 1
    for i in range(1,len(nlist)+1):
        anom *= i
    return(anom//denom)



# 大きい順に約数を並べて、dfsでなんとかならないか。
divs = make_divisors(M)
divdict = {str(div):i for i, div in enumerate(divs)} #要素に対応させる
divlist = [] #約数リスト
stack = deque([])
# 約数リスト0のところを追加しておこう
for div in divs:
    stack.append([div,M//div])

ans = 0
if N == 2:
    for div in divs:
        if div < M//div:
            ans += 2
        elif div == M//div:
            ans += 1
else:
    # 既出セット
    while len(stack) > 0:
        nlist = stack.pop()
        div = nlist[-2]
        divided = nlist[-1]
        # 割った数よりは小さい値で割っていく
        ind = divdict[str(div)]
        for div in divs[ind:]:
            if len(nlist) < N and divided%div == 0:
                new = nlist[:-1]+[div, divided//div]
                stack.append(new)
                # 指定まで溜まったら
                if len(new) == N:
                    prod = nlist[0]
                    for i in range(1,N):
                        prod *= new[i]
                    if new[-1] <= new[-2] and prod==M: #順序保証と積の保証
                        ans += count(new)


print(ans%(10**9+7))
"""