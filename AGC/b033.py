H, W, N = map(int,input().split())
sr,sc = map(int,input().split())

def manhattan(A,B):
    return(abs(A[0]-B[0])+abs(A[0]-B[0]))

# di = {"L":(-1,0),"R":(1,0),"U":(0,-1),"D":(0,1)}

S = input()
T = input()
# S = [di[s] for s in input().split()]
# T = [di[s] for s in input().split()]

flg = True

for s,t in zip(S,T):
    # takahashi
    if sc <= W//2 and sr <= H//2:
        if s == "R":
            sc += 1
        elif s == "U":
            sr += 1
    elif sc > W//2 and sr <= H//2:
        if s == "L":
            sc -= 1
        elif s == "U":
            sr += 1
    elif sc <= W//2 and sr > H//2:
        if s == "R":
            sc += 1
        elif s == "D":
            sr -= 1
    else:
        if s == "L":
            sc -= 1
        elif s == "D":
            sr -= 1
    print("Takahashi",sr,sc)    
    # aoki
    if sc <= W//2 and sr <= H//2:
        if s == "L":
            sc -= 1
        elif s == "D":
            sr -= 1
    elif sc > W//2 and sr <= H//2:
        if s == "R":
            sc += 1
        elif s == "D":
            sr -= 1
    elif sc <= W//2 and sr > H//2:
        if s == "L":
            sc -= 1
        elif s == "U":
            sr += 1
    else:
        if s == "R":
            sc += 1
        elif s == "U":
            sr += 1
    print("Aoki",sr,sc)
    if sc < 1 or sr < 1 or sc > W or sr > H:
        flg = False
        break

if flg:
    print("YES")
else:
    print("NO")
