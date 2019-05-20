S = input()
a = int(S[:2])
b = int(S[2:])
if 0 < a <= 12 and 0 < b <= 12:
    print("AMBIGUOUS")
elif 0 < a <= 12 and (b == 0 or b > 12):
    print("MMYY") 
elif 0 < b <= 12 and (a == 0 or a > 12):
    print("YYMM")
else:
    print("NA")