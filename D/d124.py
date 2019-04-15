N, K = map(int,input().split())
S = input()
nums = []
tmp = S[0]
init = int(tmp)
count = 0
for s in S:
    if tmp == s:
        count += 1
    else:
        nums.append(count)
        count = 1
        tmp = s

if init == 0:
    #始め0の場合
    lenmax = sum(nums[:2*K])
    #それ以外は1ことばし
    for i in range(1,len(nums)-2*K,2):
        if i + 2*K == len(nums):
            lenmax = max(lenmax,sum(nums[i:i+2*K]))
        else:
            lenmax = max(lenmax,sum(nums[i:i+2*K+1]))

elif init == 1:
    lenmax = 0
    #それ以外は1ことばし
    for i in range(len(nums)-2*K,2):
        if i + 2*K == len(nums):
            lenmax = max(lenmax,sum(nums[i:i+2*K]))
        else:
            lenmax = max(lenmax,sum(nums[i:i+2*K+1]))

print(lenmax)
