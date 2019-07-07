N,D = map(int, input().split())
field = []
for i in range(N):
    field.append(list(map(int, input().split())))


def calc(i,j):
    dist2d = [x**2 for x in range(200)]
    ci = field[i]
    cj = field[j]
    dist2 = [(di-dj)**2 for di,dj in zip(ci,cj)] 

    
    if sum(dist2) in dist2d:
        return True
    else:
        return False

ans = 0
for i in range(N):
    for j in range(i+1,N):
        ans += calc(i,j)

print(ans)