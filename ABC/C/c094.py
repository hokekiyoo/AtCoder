"""
中央値

2 4 4 3
2 3 4 4
真ん中の2つの値を取り出す
⇨
"""

N = int(input())
Xs = list(map(int, input().split()))
X_sort = sorted(Xs)
M1 = X_sort[N//2-1]
M2 = X_sort[N//2]
# print(X_sort,M1,M2)

for x in Xs:
    if x <= M1:
        print(M2)
    else:
        print(M1)
