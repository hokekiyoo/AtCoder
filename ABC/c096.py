"""
孤立点を見つけるだけ？
"""

h,w = map(int, input().split())
fields = []
for i in range(h):
    s = list(input())
    fields.append(s)

mvs = [(0,1),(0,-1),(1,0),(-1,0)]
for i in range(h):
    for j in range(w):
        if fields[i][j] == "#":
            cnt = 0
            for dy,dx in mvs:
                next_y,next_x = i+dy,j+dx# 次の選び方を
                if 0 <= next_y < h and 0 <= next_x < w:
                    if fields[next_y][next_x] == "#":
                        cnt += 1
            if cnt == 0:
                print("No")
                exit()


print("Yes")