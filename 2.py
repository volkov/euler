sum=0
prev=1
cur=1
while cur<=4000000:
  if cur%2==0:
    sum+=cur
  next=cur+prev
  prev=cur
  cur=next
print sum
