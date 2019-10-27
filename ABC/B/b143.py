N = int(input())
ds  = list(map(int, input().split()))
ans = 0
for i in range(N):
    for j in range(i+1,N):
        ans += ds[i]*ds[j]
print(ans)