from datetime import date
from datetime import timedelta
start = date(1901,1,1)
end = date(2000,12,31)
day = timedelta(days=1)
current = start
res = 0
while current<=end:
  if current.weekday()==6 and current.day==1: res+=1
  current+=day 
print("result",res) 
