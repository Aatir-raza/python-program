# empty
s=set()
print(s)
print(type(s))

# 1d and 2d 
s1={1,2,3}
print(s1)
# s2={1,2,3{4,5}}
# print(s1)
# homo and hetro
s3={1,'hello',4.5,(1,2,3)}
print(s3)
# using type conversion 
s4=set([1,2,3])
print(s4)
# duplicate not allowed
s5={1,1,2,2,3,3}
print(s5)

# set cannot have mutable items
s1={1,2,3}
s2={3,2,1}
print(s1==s2)
