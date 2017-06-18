for i in range(1,334):
  for j in range(i,500):
    k = 1000-i-j
    if i**2+j**2==k**2:
      print "{} {} {}".format(i,j,k)
      print i*j*k
