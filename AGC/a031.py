N = int(input())
S = input()

alphabets = "abcdefghijklmnopqrstuvwxyz"
ans = 1
for alphabet in alphabets:
    cnt = S.count(alphabet)
    ans *= (cnt+1)
ans -= 1
print(ans%(10**9+7))

