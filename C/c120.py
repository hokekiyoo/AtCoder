S = input()
num1 = S.count("1")
num0 = S.count("0")
print(len(S)-abs(num0-num1))