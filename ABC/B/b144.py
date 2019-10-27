N = int(input())
flg = False
for i in range(9,0,-1):
    if N % i == 0 and N//i <= 9:
        flg =True
        break
if flg:
    print("Yes")
else:
    print("No")