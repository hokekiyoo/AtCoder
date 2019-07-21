"""
x -> y -> x^y ->
x -> y -> x^y

3つ周期。
N%3 != 0 x=y=x^yなので、全部0
N%3 == 0 x,y,x^yが同数存在
"""

N = int(input())
As = list(map(int, input().split()))
numset = sorted(list(set(As)))
n = len(numset)
if n == 1:
    if sum(As) == 0: print("Yes")
    else:print("No")
elif n == 2:
    n1 = As.count(numset[0])
    n2 = As.count(numset[1])
    if 2*n1 == n2 and numset[0] == 0: print("Yes")
    else:print("No")
elif n == 3:
    n1 = As.count(numset[0])
    n2 = As.count(numset[1])
    n3 = As.count(numset[2])
    if n1 == n2 == n3 and (numset[0]^numset[1]^numset[2])==0: print("Yes")
    else: print("No")
else:
    print("No")