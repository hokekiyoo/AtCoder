N,K = map(int, input().split())
As  = list(map(int, input().split()))
# 約数
As = sorted(As)
def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)
    return divisors

divs = sorted(make_divisors(sum(As)),reverse=True)

from itertools import accumulate
for div in divs:
    # 足す側と引かれる側を分け
    # 小さい順にソートして、足し引きのプラマイが0になれば良い。
    # ただし、足す大きさ(=引く大きさ)がKを超えるといけない
    bs_plus = sorted([a%div for a in As])
    bs_minus = [(div-a)%div for a in bs_plus]
    acc_bs_p = list(accumulate(bs_plus))
    acc_bs_m = list(accumulate(bs_minus))
    for i in range(N):
        plus = acc_bs_p[i]
        minus = acc_bs_m[N-1]-acc_bs_m[i]
        if plus == minus and plus <= K:
            # print("ok",div,plus,minus)
            print(div)
            exit(0)
        
