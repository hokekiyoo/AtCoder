from collections import Counter
S = input()
T = input()

import numpy as np
S_num = dict(Counter(S)).values()
T_num = dict(Counter(T)).values()
Ss = np.array([s for s in S_num])
Ts = np.array([s for s in T_num])

if len(Ss) != len(Ts):
    print("No")
else:
    if all(np.sort(Ss)==np.sort(Ts)):
        print("Yes")
    else:
        print("No")

## 別解？
"""
普通にsortedとできるっぽい。わざわざnumpy配列にしなくてOK
from collections import Counter
s, t = input(), input()
c1 = sorted(Counter(s).values())
c2 = sorted(Counter(t).values())
print('Yes') if c1 == c2 else print('No')
"""