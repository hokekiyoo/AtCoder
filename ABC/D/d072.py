N = int(input())
ps = list(map(int,input().split()))
# p_swap = [-1]*N
ans = 0
for i in range(N-1):
    if i+1 == ps[i]:
        p1,p2 = ps[i:i+2]
        ps[i] = p2
        ps[i+1] = p1
        ans += 1
if ps[N-1] == N:
    ans += 1
print(ans)