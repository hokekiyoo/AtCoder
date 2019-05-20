N, K = map(int,input().split())
# aの桁数
a = len(bin(K))-2
c = 0
# print(a)
# 引いたときにK-1以下である確率
prob1 = min(1,(K-1)/N)
prob2 = 1-prob1

cnt = 0
ans = 0
while (K-1)//(2**cnt) > 0:
    #そこに収まる数(maxがN)
    n = min(N, (K-1)//(2**cnt)) - (K-1)//(2**(cnt+1))
    if n > 0:
       ans += n*1.00/(N*2**(cnt+1))
    #    print(cnt+1,n,ans)
    cnt+=1
    
print(ans+prob2)