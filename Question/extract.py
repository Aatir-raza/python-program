# EXTRACT USERNAME FROM A GIVEN EMAIL.
#Eg if the email is aatir24raza@gmail.com
# then the username should be AAtir24raza

s= input('enter the email')
pos=s.index('@')

print(s[0:pos])