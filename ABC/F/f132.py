from itertools import accumulate

N,K = map(int, input().split())
As = [] 
for i in range(1,int(N**0.5)+1):
    As.append(i)
    if N//i != i:
        As.append(N//i)
As = sorted(As,reverse=False)
nums = []
for i in range(len(As)-1):
    nums.append(As[i+1]-As[i])
nums = [1] + nums
nums.reverse()
mod = 10**9 + 7
ans = 0
dp = [[0] * len(As) for i in range(K+1)]


dp[0][0] = 1
for i in range(K):
    # 1だと全通り分が成り立つし、Nだと1通り。
    # それぞれ種別にまとまっているので、それらをかける
    acc = list(accumulate(dp[i]))
    for j in range(len(As)):
        dp[i+1][len(As)-j-1] = acc[j]*nums[j]%mod
print(sum(dp[K])%mod)
