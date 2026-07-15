# find the sum of a 3 digit number entered by the user

number = int(input('enter a 3 digit number'))
#345 % 10
a = number % 10
number =  number//10
#34 % 10
b = number % 10
number = number// 10
# 3% 10 
c = number % 10
print( a+b+c)