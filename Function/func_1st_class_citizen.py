# type and id 
def square(num):
  return num**2
print(type(square))
a=2
print(id(a))

# reassign 
x=square
print(id(x))
x(3)
# deleting a function
#del square 

# storing
L=[1,2,3,4,square]
print(L[-1](3))

# returning a function
def f():
  def x(a,b):
    return a+b
  return x
val=f()(3,4)
print(val)
# function as argument 
def func_a():
  print('inside func_a')
def func_b(z):
  print('inside func_c')
  return z()
print((func_a)) 
