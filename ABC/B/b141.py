S = input()
S_ki = S[0::2]
S_gu = S[1::2]

import sys
for k in S_ki:
    if k == "L":
        print("No")
        sys.exit()
for g in S_gu:
    if g == "R":
        print("No")
        sys.exit()
print("Yes")