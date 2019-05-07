from itertools import accumulate

N, K = map(int,input().split())
S = input()

nums = []
tmp = "1" #はじめに0が入ったら、0からスタートというのがわかる。
count = 0
for s in S:
    if tmp == s:
        count += 1
    else:
        nums.append(count)
        count = 1
        tmp = s
nums.append(count)
if tmp == "0":
    nums.append(0) #エッジの条件

# print(nums)
# 累積和表示にする(listって足し算できるのね)
# これによって、各文字最初の値が明らかになる
acc = [0]+list(accumulate(nums))
# print(acc)
n = len(nums)
w = 2*K + 1

if len(nums) <= w:
    print(N)
else:
    ans = 0
    for i in range(0,n-w+1,2): #2個飛ばし
        ans = max(ans,acc[i+w]-acc[i])

    print(ans)