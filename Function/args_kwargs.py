def multiply (*args):
  product=1
  for i in args:
   product=product*i
  return product    
print(multiply(2,3,4))
# **kwargs
def display(**kwargs):
  for(key,value) in kwargs.items():
    print(key,'>',value)
display(india='delhi',srilanka='colombo',nepal='kathmandu',pakistan='islamabad')
    

    