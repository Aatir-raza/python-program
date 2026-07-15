#x->x^2
a=lambda x:x**2
print(a(2))
# x,y -> x+y
a=lambda x,y:x+y
print(a(5,2))

# check if a string has a 
a= lambda s:'a' in s
print(a('hello'))
# odd or even 
a=lambda x:'even' if x%2==0 else'odd'
print(a(6))

