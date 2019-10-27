N, K, Q = map(int, input().split())
points = [K-Q]*(N)
for i in range(Q):
    A = int(input())
    A -= 1
    points[A] += 1
# print(points)
for p in points:
    if p >0:
        print("Yes")
    else:
        print("No")