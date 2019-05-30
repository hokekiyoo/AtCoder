"""
combination
右が固定 : 左は大きければ大きいほうが良い
左が固定 : 右は1/2に近ければ近いほうが良い
これを左から順に探していくので良い
"""

N = int(input())
As = list(map(int,input().split()))
As = sorted(As, reverse=True)
l = As[0]
r = As[1]

for a in As[2:]:
    if abs(l/2-a) < abs(l/2-r):
        r = a
print(l,r)