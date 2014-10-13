#numbers  = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
for num in range(1,51):
    if num%3 == 0 and not num%5 == 0:
      print 'fizz'
    elif num%5 == 0 and not num%3 == 0:
      print 'buzz'
    elif num%3 == 0 and num%5 == 0:
      print 'fizzbuzz'
    else:
      print num