N = int(input())
S = input()
prev = S[0]
cnt = 1
for i in range(1,N):
    if prev == S[i]:
        continue
    else:
        prev = S[i]
        cnt += 1
print(cnt)