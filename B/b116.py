def f(n):
    if n%2 == 0:
        return int(n/2)
    else:
        return int(3*n+1)


s = int(input())

collatz = [s]
count = 1
continue_flg = True
while continue_flg:
    collatz_nums = set(collatz)
    count += 1
    s = f(s)
    for collatz_num in collatz_nums:
        if collatz_num == s:
            continue_flg = False
    collatz.append(s)
print(count)