n = int(input())
ps = list(map(int, input().split()))
cnt = 0
for i in range(n-2):
    p0 = ps[i]
    p1 = ps[i+1]
    p2 = ps[i+2]
    if p0 < p1 and p1 < p2:
        cnt += 1
    elif p2 < p1 and p1 < p0:
        cnt += 1
print(cnt)