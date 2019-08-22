from collections import defaultdict
N = int(input())
d = defaultdict(int)

for i in range(N):
    s = str(sorted(input()))
    d[s] += 1
ans = 0

for key in d.keys():
    ans += d[key]*(d[key]-1)//2
print(ans)



# N = int(input())
# alphabet = "abcdefghijklmnopqrstuvwxyz"

# from collections import defaultdict
# d = defaultdict(int)
# for i in range(N):
#     s = input()
#     num = 0
#     sorted(alphabet)
#     for i,a in enumerate(alphabet):
#         if s.count(a) == 10:
#             continue #アナグラムはない
#         num += s.count(a)*10**i
#     d[num] += 1

# ans = 0

# for key in d.keys():
#     ans += d[key]*(d[key]-1)//2
# print(ans)

