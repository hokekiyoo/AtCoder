N, Y = map(int,input().split())
a_max = min(N, Y // 10000)
flg = False
for a in range(a_max+1):
    if flg: 
        break
    for b in range(N+1):
        if flg:
            break 
        c = N - a - b
        if a*10000+b*5000+c*1000 == Y and c >= 0:
            print(a,b,c)
            flg = True
if not flg:
    print(-1,-1,-1)