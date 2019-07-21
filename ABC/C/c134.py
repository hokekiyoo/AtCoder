N = int(input())
first = 0
second = 0
As = []
for i in range(N):
    n = int(input())
    As.append(n)
    if first < n:
        first = n
    elif second < n:
        second = n

for a in As:
    if a == first:
        print(second)
    else:
        print(first)