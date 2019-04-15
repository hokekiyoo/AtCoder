S = input()
n = len(S)
i = n%2
As = []
Bs = []
if i == 0:
    As = "01"*(n//2)
    Bs = "10"*(n//2)
elif i == 1:
    As = "01"*(n//2)+"0"
    Bs = "10"*(n//2)+"1"
count_A,count_B = 0,0
for A,B,s in zip(As,Bs,S):
    print(A,B,s)
    count_A += (int(A)+int(S))%2
    count_B += (int(B)+int(S))%2
print(min(count_A,count_B))