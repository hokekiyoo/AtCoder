k,x = map(int, input().split())

nmin = x - k + 1
nmax = x + k - 1

ans = [i for i in range(nmin,nmax + 1)]
print(*ans)
