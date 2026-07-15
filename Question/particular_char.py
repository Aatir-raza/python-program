# WRITE A PROGRAM WHICH CAN REMOVE A PARTICULAR CHARACTER FROM A STRING 

s=input('enter the string')
term=input('what would like to remove')

result = ''
for i in s:
  if i != term:
    result=result+i
print(result)    