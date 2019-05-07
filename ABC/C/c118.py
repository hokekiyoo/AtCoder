import numpy as np

N = int(input())
As = input().split()
As = [int(A) for A in As]


def gcd(a, b):
  while b > 0:
    a, b = b, a%b
  return a

min_HP = np.inf
a0 = As[0]
for a in As[1:]:
    b = gcd(a0,a)
    if b <= a0:
        a0 = b
print(a0)

