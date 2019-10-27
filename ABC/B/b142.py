n,k = map(int, input().split())
hs = sorted(list(map(int, input().split())),reverse=True)
cnt = 0
for h in hs:
    if h >= k:
        cnt += 1
print(cnt)    