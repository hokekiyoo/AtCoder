S = input()
s = set(S)
flg = True
for a in s:
    n = S.count(a)
    if n!=2:
        flg = False
        break
if flg:
    print("Yes")
else:
    print("No")