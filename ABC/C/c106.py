S = input()
K = int(input())

"""
Sが2なら22,3なら333,4なら4444
nならstr(n)*n
5000兆日後のK文字目は何か

1234
1223334444
12222333333333444444444444444
i日後にはn^i増えてる

"""
# 頭が1
# どこまで1を持っているか調べておく
if S[0] == "1":
    for ind,s in enumerate(S):
        if s != "1":
            break
    ind += 1
    if K < ind:
        print(1)
    else:
        print(s)
else:
    print(S[0])   