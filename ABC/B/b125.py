N = int(input())
Vs = [int(i) for i in input().split()]
Cs = [int(i) for i in input().split()]

diff = [max(v-c,0) for v,c in zip(Vs,Cs)]
print(sum(diff))