import numpy as np
N = int(input())
hs = input().split()
hs = np.array([int(h) for h in hs])

# hs = np.array([0,4,23,75,23,0,96,50,100])

def split_array(hs):
    split_indexes = np.where(hs==0)[0]
    n = len(split_indexes)
    split_list = []
    if n > 0:
        split_list.append(hs[0:split_indexes[0]])
        if n > 1:
            for i in range(n-1):
                split_list.append(hs[split_indexes[i]+1:split_indexes[i+1]])
        split_list.append(hs[split_indexes[-1]+1:])
    return split_list

def make_shower(l):
    count = l.min()
    return count, l-count

all_count = 0
c, hs = make_shower(hs)
split_list = split_array(hs)
all_count += c
zero_count = 0
#全部のリストが空になったところで終了
while True:
    zero_count = 0
    split_list_new = []
    for l in split_list:
        if len(l) == 0:
            zero_count += 1
            continue
        count, l_showered = make_shower(l)
        # print("count",count,l,l_showered)
        all_count += count
        split_list_ = split_array(l_showered)
        split_list_new.extend(split_list_)

    len_split_list = len(split_list) # リストの長さを取っておく
    split_list = [l for l in split_list_new] #代入
    
    if zero_count == len_split_list:
        break
print(all_count)
