"""
競プロ幼稚園には
N人の子供がいます。えび先生は、子供たちを一列に並べ、一人目にはキャンディーを
1個,二人目には2個,...,N人目にはN個あげることにしました。必要なキャンディーの個数の合計は何個でしょう?
"""
N = int(input())
print(int(N*(N+1)/2))