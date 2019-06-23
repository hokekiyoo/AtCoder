n,l = map(int, input().split())
aji = [l+i for i in range(n)]


min_aji = 10**9+7
ind = 0
for i in range(n):
    if min_aji > abs(aji[i]):
        ind = i
        min_aji = abs(aji[i])

print(sum(aji)-aji[ind])