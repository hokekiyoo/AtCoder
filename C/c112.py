import numpy as np
N = int(input())
data = np.zeros((N,3))
for i in range(N):
    data[i] = np.array(input().split())

# data = np.array([[2,3,0],[2,1,0],[1,2,0],[3,2,5]])

if len(np.where(data[:,2]!=0)[0]) == 1:
    C_x, C_y, H = map(int,data[np.where(data[:,2]!=0)[0][0]])
    print(C_x, C_y, H)
else:
    for n in range(10201):
        C_x = n // 101
        C_y = n % 101
        correctflg = True
        unsetflg = True
        for x,y,h in data:
            if unsetflg:
                if h >= 1:
                    H = abs(x-C_x)+abs(y-C_y)+h
                    unsetflg = False
            else:
                if h >= 1 and H != abs(x-C_x)+abs(y-C_y)+h:
                    correctflg = False
                    break 
        if correctflg:
            print(C_x,C_y,int(H))
            break
        
            
            
