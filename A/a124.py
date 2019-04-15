A,B = map(int,input().split())
print(max(max(A+B,2*A-1),2*B-1))