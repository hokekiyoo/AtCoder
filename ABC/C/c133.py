L,R = map(int, input().split())


diff = R - L
ans = 2019
if diff >= 2019:
    print(0)
else:
    for i in range(diff+1):
        for j in range(i+1,diff+1):
            l = (L+i)
            r = (L+j)
            ans = min(ans,(l*r)%2019)
    print(ans)