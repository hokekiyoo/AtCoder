N, K = map(int,input().split())
q = list(map(int,input().split()))

# 何個捨てるか
ans = 0
for i in range(K):
    # 右から何個目まで取るか
    if K-i >= N:
        pick = q
        pick = sorted(pick)
        for m in range(i+1):
            ans = max(sum(pick[m:]),ans)        
    else:
        pick = q[:K-i]
        pick = sorted(pick)
        ans = max(sum(pick[i:]),ans)
        for j in range(min(N,K-i)):
            pick = []
            pick = q[:j]+q[-(K-i-j):]
            pick = sorted(pick)
            for m in range(i+1):
                ans = max(sum(pick[m:]),ans)        
print(ans)