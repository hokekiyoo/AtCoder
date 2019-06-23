n,k = map(int, input().split())
max_connect = (n-1)*(n-2)//2
if k > max_connect:
    print(-1)
else:
    print(n+max_connect - k -1)
    for i in range(n-1):
        print(i+1,n)

    end = max_connect - k
    cnt = 0
    cntflg = end > 0
    for i in range(n-1):
        for j in range(i+1,n-1):
            if cntflg:
                print(i+1,j+1)
                cnt += 1
            if cnt == end:
                cntflg = False