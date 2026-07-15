# number greater than 5
L=[2,3,4,5,6]
print(list(filter(lambda x:x>5,L)))
# fetch fruits starting with a 
fruits=['apple','guava','chessy']
print(list(filter(lambda x:x.startswith('a'),fruits)))

# reduce 
# sum of all items
import functools
print(functools.reduce(lambda x,y:x+y,[1,2,3,4,5]))

# find min 
print(functools.reduce(lambda x,y:x if x<y else y,[23,11,45,10,9]))

