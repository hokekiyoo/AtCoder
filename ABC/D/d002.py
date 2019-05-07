"""
派閥に含まれるすべての議員は互いに知り合いでなければなりません。
どの2頂点を選んでも辺でつながる。⇨クリークという
最大クリーク問題
http://www.tani.cs.chs.nihon-u.ac.jp/g-2006/s5402031hide/maxclq_last.pdf
"""
def enumerate_pair(index):
    pairs = []
    n = len(index)
    i = 0
    while i <= n:
        for j in range(i+1, n):
            pairs.append([index[i],index[j]])
        i += 1
    return pairs

def check_pairs(correct_pairs,pairs):
    flg = True
    for correct_pair in correct_pairs:
        if sorted(correct_pair) not in pairs:
            flg = False
    return flg

N, M = map(int,input().split())
if M == 0:
    print(1)
else:
    """失敗例
    連結する全ての頂点ではなく、『互いに知り合い』な集合
    """
    pairs = []
    for i in range(M):
        x, y = map(int,input().split())
        pairs.append([min(x,y),max(x,y)])

    max_party = 2
    for n in range(2**N):
        nstr = "{:013b}".format(n)[-N:]
        indexes = [i+1 for i,b in enumerate(nstr) if b == "1"]
        if len(indexes) <= 2:
            continue
        correct_pairs = enumerate_pair(indexes)
        # print(check_pairs(correct_pairs,pairs))
        if check_pairs(correct_pairs,pairs):
            print(indexes)
            max_party = max(max_party,len(indexes))
    print(max_party)



    # pairs = [[int(i) for i in input().split()]]
    # for i in range(M-1):
    #     x, y = map(int,input().split())
    #     flg_append = True
    #     for pair in pairs:
    #         if x in pair and y in pair:
    #             flg_append = False
    #         elif x in pair:
    #             pair.append(y)
    #             flg_append = False
    #         elif y in pair:
    #             pair.append(x)
    #             flg_append = False
    #     if flg_append:
    #         pairs.append([x,y])
    # relation_max = 0 
    # for pair in pairs:
    #     relation_max = max(len(set(pair)),relation_max)
    # print(relation_max)
