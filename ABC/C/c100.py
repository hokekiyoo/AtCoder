N = int(input())
As = list(map(int, input().split()))
"""
3
5 2 4
2^xについて調べる
"""

ans = 0
for a in As:
    while True:
        if a%2 == 0:
            ans += 1
            a //= 2
        else:
            break
print(ans)