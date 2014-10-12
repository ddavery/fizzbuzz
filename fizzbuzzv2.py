import sys
if len(sys.argv) == 1:
  guess = int(raw_input('Enter an integer : '))
  if guess%3 == 0 and not guess%5 == 0:
    print 'fizz'
  elif guess%5 == 0 and not guess%3 == 0:
    print 'buzz'
  elif guess%3 == 0 and guess%5 == 0:
    print 'fizzbuzz'
  else:
    print guess
else:
 s = int(sys.argv[-1])
 if s%3 == 0 and not s%5 == 0:
   print 'fizz'
 elif s%5 == 0 and not s%3 == 0:
   print 'buzz'
 elif s%3 == 0 and s%5 == 0:
   print 'fizzbuzz'
 else:
   print s