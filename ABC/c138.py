
N = int(input())
vs  = sorted(list(map(int, input().split())))
ans = 0
ans = vs[0]+vs[1]
for i,v in enumerate(vs[2:]):
    ans += v*2**(i+1)
print(ans)
ans/=2**(N-1)
print(ans)