ls = list(map(int, input().split()))
ls.sort(reverse=True)
a = ls[0]
if a%2 == 0:
    print(0)
else:
    print(ls[1]*ls[2])