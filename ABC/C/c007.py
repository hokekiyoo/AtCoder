import numpy as np #numpyの読み込みは200msくらいロス
from collections import deque

R,C = map(int,input().split())
sy,sx = map(int,input().split())
gy,gx = map(int,input().split())
matrix = []
for _ in range(R):
    rows = [s for s in input()]
    matrix.append(rows)
# tokuten = [[0]*C]*R
tokuten = np.zeros((R,C))
l = deque([(sy-1,sx-1)])
tokuten[sy][sx] = 0
matrix[gy-1][gx-1]="g"
matrix[sy-1][sx-1] = "#"

while len(l) != 0:
    y,x = l.popleft()
    # print(y,x)
    up = matrix[y-1][x]
    if up == ".":
        l.append((y-1,x))
        tokuten[y-1][x] = tokuten[y][x] + 1
        matrix[y-1][x] = "#" #一回一回やらないと再探索が入ってめんどくさい
    elif up == "g":
        print(int(tokuten[y][x] + 1))
        break

    down = matrix[y+1][x]
    if down == ".":
        l.append((y+1,x))
        tokuten[y+1][x] = tokuten[y][x] + 1
        matrix[y+1][x] = "#"
    elif down == "g":
        print(int(tokuten[y][x]+1))
        break

    left = matrix[y][x-1]
    if left == ".":
        l.append((y,x-1))
        tokuten[y][x-1] = tokuten[y][x] + 1
        matrix[y][x-1] = "#"
    elif left == "g":
        print(int(tokuten[y][x]+1))
        break

    right = matrix[y][x+1]
    if right == ".":
        l.append((y,x+1))
        tokuten[y][x+1] = tokuten[y][x] + 1
        matrix[y][x+1] = "#"
    elif right == "g":
        print(int(tokuten[y][x]+1))
        break
