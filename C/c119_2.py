import numpy as np

N, A, B, C = map(int,input().split())
goals = [A,B,C]
ls = []
for i in range(N):
    ls.append(int(input()))

# goals = [1000,800,100]
# ls = [300,333,400,444,500,555,600,666]

def count(x,ls):
    try:
        x.index(0)
        x.index(1)
        x.index(2)        
    except:
        return False
    A = np.zeros(len(goals))
    for i,l in enumerate(ls):
        add_ind = x[i]
        if add_ind==3:
            pass
        else:
            A[add_ind] += l
    combine_MP = 0
    for i in range(3):
        combine_MP += 10*(x.count(i)-1)
    return A, combine_MP
    
    
score_min = 100000
for N in range(4**8):
    x = []
    for j in range(len(ls)):
        x.append(N % 4)
        N = N // 4 
    try:
        A, combine_MP = count(x,ls)
        score = np.abs(A-np.array(goals)).sum() + combine_MP
        if score_min >= score:
            score_min = score
    except:
        pass
print(score_min)