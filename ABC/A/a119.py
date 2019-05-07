from datetime import datetime as dt
date0 = dt(2019,4,30)
date = input()
tdate =dt.strptime(date, '%Y/%m/%d')
if date0 >= tdate:
    print("Heisei")
else:
    print("TBD")