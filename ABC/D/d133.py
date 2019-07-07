N = int(input())
As = list(map(int, input().split()))
A_all = sum(As)//2
ans = [0]*N

a0 = sum(As[1:N:2])
ans[0] = (A_all-a0)
for i in range(1,N):
    ans[i] = As[i-1]-ans[i-1]

ans = [a*2 for a in ans]
print(*ans)