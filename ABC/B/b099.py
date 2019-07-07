a,b = map(int, input().split())

diff = b-a
H = diff*(diff-1)//2
print(H-a)
