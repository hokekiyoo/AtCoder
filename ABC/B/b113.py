N = int(input())
T,A = map(int,input().split())
Hs = list(map(int,input().split()))

diff_T = [abs(T-h*0.006-A) for h in Hs]
print(diff_T.index(min(diff_T))+1)