N = int(input())
print(min([111*i-N for i in range(1,10) if 111*i>=N])+N)
