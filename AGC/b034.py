S = input()
S = S.replace("BC","D")
cnt_A = 0
ans = 0
for s in S:
    if s == "A":
        cnt_A += 1
    elif s == "D":
        ans += cnt_A 
    else:
        cnt_A = 0
print(ans)