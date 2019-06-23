S = input()
flg = True
s = S[0]
for i in range(1,4):
    if s == S[i]:
        flg = False
    s = S[i]

if flg:
    print("Good")
else:
    print("Bad")