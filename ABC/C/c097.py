"""
sの異なる部分文字列のうち、
辞書順でK番目に小さいもの
|s| <= 5000
"""

s = input()
K = int(input())
n = len(s)
substrs = set()
for i in range(n):
    for j in range(K):
        if i + j >= n:
            continue
        substrs.add(s[i:i+j+1])
print(sorted(substrs)[K-1])
    
