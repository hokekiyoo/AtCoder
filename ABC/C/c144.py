N = int(input())
sqN = int(N**0.5)+1
for i in range(sqN,0,-1):
    if N % i == 0:
        ans = i+N//i
        break

print(ans-2)