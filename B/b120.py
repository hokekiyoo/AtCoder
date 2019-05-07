A,B,K = map(int,input().split())
cnt = 0
l = []
for i in range(max(A+1,B+1),0,-1):
    if A%i == 0 and B%i == 0:
        cnt +=1
        if cnt == K:
            ans = i
            break
print(ans)