# default argument
def power(a=1,b=1):
  return a**b
print(power(2))

# positional argument
print(power(2,3))

# keyword argument
print(power(b=3,a=2))