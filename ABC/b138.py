N = int(input())
As  = list(map(int, input().split()))

rev = 0
for a in As:
    rev += 1/a
print(1/rev)