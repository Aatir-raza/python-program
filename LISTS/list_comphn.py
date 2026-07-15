# scalar multipilication on a vector 
v=[2,3,4]
s=-3
# [-6,-9,-12]
print([s*i for i in v])
# add squares
L=[1,2,3,4,5]
print([i**2 for i in L])

# print all number divisible by 5 in the range of 1 to 50

print([i for i in range(1,51) if i%5==0])

# find the language which start with letter p;
Languages=['java','python','php','c','javascript']
print([i for i in Languages if i .startswith('p')])

# nested if with list comprehension
basket=['apple','guava','cherry','banana']
My_fruits=['apple','kiwi','grapes','banana']
print([fruit for fruit in My_fruits if fruit in basket if-fruit.startswith('a')])

# print a (3,3) matrix using list cmprehension ->nested list comprehension
print([[i+j for i in range (1,4)]  for j in range (1,4)])

# cartisian products > lists comprehension on 2 list together 
L1=[1,2,3,4]
L2=[5,6,7,8]
print([i*j for i in L1 for j in L2])
# 2 ways to transverse a list 
#itemwise
L=[1,2,3,4]
for i in L:
  print(i)

# indexwise
L=[1,2,3,4]
for i in range(0,len(L)):
  print(i)