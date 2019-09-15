As = sorted(list(map(int, input().split())))
K = int(input())

As[-1] = As[-1]*2**(K)
print(sum(As))
