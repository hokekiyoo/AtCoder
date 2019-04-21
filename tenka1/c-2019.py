from itertools import accumulate

N = int(input())
S = input()
black = [int(s=="#") for s in S]
white = [int(s==".") for s in S[::-1]]

a_black = [0]+list(accumulate(black))
a_white = list(accumulate(white))[::-1]+[0]

ans = 1000000
for b,w in zip(a_black,a_white):
    ans = min(ans, b+w)
print(ans)