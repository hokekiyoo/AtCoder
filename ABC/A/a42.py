import numpy as np
a, b, c = map(int, input().split()) 
nums = [a,b,c]
list5 = [num for num in nums if num == 5]
list7 = [num for num in nums if num == 7]
if (len(list5)==2 and len(list7)==1):
    print("YES")
else:
    print("NO")