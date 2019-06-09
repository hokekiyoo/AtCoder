"""
自分の左に並んでいた人数と自分の右に並んでいた人数の差の絶対値はAi
元の並び方が何通りあるか

N = 3
並び    1 2 3
As      2 0 2

N = 4
並び    1 2 3 4
As      3 1 1 3

2^n通りだろう
"""
N = int(input())
As = list(map(int,input().split()))
As = sorted(As)
mod = 10**9 + 7

if N % 2 == 0:
    A = [(i)//2*2+1 for i in range(N)]
    if As == A:
        print(2**(N//2)%mod)
    else:
        print(0)
else:
    A = [0] + [(i+1)//2*2 for i in range(1,N)]
    if As == A:
        print(2**((N-1)//2)%mod)
    else:
        print(0)