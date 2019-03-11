K, S = map(int,input().split())
count = 0
start = max(S - 2*K, 0)

for X in range(start,K+1):
    for Y in range(start,K+1):
        Z = S - X - Y
        if Z >= 0 and Z <= K:
            count += 1
print(count)