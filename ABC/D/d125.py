
N = int(input())
A = [int(i) for i in input().split()]
cnt = 0
for a in A:
    if a<0:
        cnt += 1
A = [abs(a) for a in A]
if cnt % 2 == 1:
    print(sum(A)-2*min(A))
else:
    print(sum(A))
