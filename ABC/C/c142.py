N = int(input())
As  = list(map(int, input().split()))

sts = [(a,i+1) for i,a in enumerate(As)]
sts = sorted(sts)
ans = []
for st in sts:
    ans.append(st[1])
print(*ans)