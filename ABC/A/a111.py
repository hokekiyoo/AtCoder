S = input()
ans = ""
for s in S:
    if s == "9":
        ans += "1"
    elif s == "1":
        ans += "9"
    else:
        ans += s
print(ans)