import sys
N = int(input())
As = list(map(int, input().split()))
cnt = 0
for i, a in enumerate(As):
    if i+1 != a:
        if As[a-1] == i+1:
            cnt +=1
        else:
            print("NO")
            sys.exit()

if cnt//2 <= 1:
    print("YES")
else:
    print("NO")