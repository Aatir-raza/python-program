# WRITE A PROGRAM THAT CAN CHECK WHETHER A GIVEN STRING IS PALINDROME OR NOT.
#ABBA
#MALAYALAM

s= input('enter the string')
flag=  True
for i in range (0,len(s)//2):
  if s[i] != s[len(s)-i-1]:
    flag= False
    print('not a palindrome')
    break
if flag:
  print('palindrome')  
