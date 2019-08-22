"""
https://atcoder.jp/contests/abc094/tasks/arc095_b
comb(n,r)
a1, a2, ..., an から2つの数をcomb(ai,aj)が最大になるように選ぶ


2 4 6 9 11
"""

n = int(input())
As  = list(map(int, input().split()))
A_sort = sorted(As)
A_max = max(As)

ans = 100000000000
for a in A_sort[:-1]:
    d1 = abs(A_max / 2 - ans)
    d2 = abs(A_max / 2 - a)
    if d1 >= d2:
        ans = a
print(A_max,ans)
