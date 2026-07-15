#minimum of 3 numbers
a= int(input('first num'))
b=int(input('second num'))
c=int(input('third num'))

if a<b and a<c:
  print('smallest is',a)
elif b<c:
  print('smallest is',b) 
else:
  print('smallest is',c)
     
