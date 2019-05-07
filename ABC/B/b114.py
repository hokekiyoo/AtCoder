S = input()
ans = 1000
for i in range(len(S)-2):
    s = S[i:i+3]
    ans = min(abs(ans-753),abs(int(s)-753))
print(ans)