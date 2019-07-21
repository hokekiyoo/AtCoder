from collections import deque

H,W = map(int, input().split())
board = [["#"]*(W+2)]
for i in range(H):
    board.append(["#"]+list(input())+["#"])
board.append(["#"]*(W+2))
board[H][W] = "g" 

# #を数えておく
cntsharp = 0
for i in range(1,H+1):
    for j in range(1,W+1):
        if board[i][j] == "#":
            cntsharp += 1

# BFS
seen = [[-1] * (W+2) for i in range(H+2)]
seen[1][1] = 0 # 始めどこから行くか
q = deque([[1,1,1]]) #h,w,p
mvs = [(1,0),(-1,0),(0,1),(0,-1)]

# print(cntsharp)
while len(q) > 0:
    h,w,p = q.popleft()
    # h,w,p = li[0],li[1],li[2]
    for dh,dw in mvs: 
        next_h = h + dh
        next_w = w + dw
        next_p = p + 1
        if seen[next_h][next_w] == -1 and board[next_h][next_w] != "#":
            seen[next_h][next_w] = next_p
            q.append([next_h,next_w,next_p])
            
if seen[H][W] == -1:
    print(-1)
else:
    print(H*W-cntsharp-seen[H][W])