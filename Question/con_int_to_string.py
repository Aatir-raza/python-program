number=int(input('enter the number'))
digit= '0123456789'
result=' '
while number != 0:
  result = digit[number%10]+result
  number=number//10

print(result)
print(type(result))



