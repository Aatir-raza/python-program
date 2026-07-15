def square (x):
  return x**2
def transform(f,L):
  output=[]
  for i in L:
    output.append(f(i))
  print(output)
L=[1,2,3,4,5] 
print(transform(square,L))

# map 
# square the item of a list
list(map(lambda x:x**2,[1,2,3,4,5]))
# odd/even/ labelling of list items
L=[1,2,3,4,5,6]
list(map(lambda x:'even' if x%2==0 else'odd',L))

# fetch names from a list of dict
users=[
  {
    'name':'rahul',
    'age':45,
    'gender':'male'
  },
  { 
    'name':'aatir',
    'age': 20,
    'gender':'male'
  },
  {
    'name':'almash',
    'age':22,
    'gender':'male'

  }
]

print(list(map(lambda user:user['name'],users)))
