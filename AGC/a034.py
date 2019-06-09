N, A, B, C, D = map(int,input().split())
S = input()
# ふぬけ が すぬけ より前にいる
if C < D:
    S_cut = S[A-1:D]
    num = S_cut.count("##")
    # print(S_cut)
    if num > 0:
        print("No")
    else:
        print("Yes")
# すぬけ が ふぬけ より前にいる
else:
    S_cut1 = S[A-1:C]
    # 飛び越えられる
    flg1 = (S_cut1.count("##") == 0)
    # S_cut2 = S[max(0,B-2):D+1]
    S_cut2 = S[A-1:D+1]    
    # 抜く場所
    flg2 = (S_cut2.count("...")>=1)
    if flg1 and flg2:
        print("Yes")
    else:
        print("No")
