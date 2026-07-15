# empty dict
d={}
print(d)
# 1d dictionary
d1={'name','aatir','gender','male'}
print(d1)
# with mixed keys
d2={(1,2,3): 1,'hello':'world'}
print(d2)
# 2d dictionary
s={'name':'aatir',
   'college':'cit',
   'sem':4,
   'subjects':{'dsa':50,
               'maths':67,
               'english':34,
               }
         }
#add key value pair
s['subjects']['dsa']=75
s['sem']=5
print(s)

# using sequence and dict function. 
d4=dict([(1,1),(2,2),(3,3)])
print(d4)
# duplicate keys 
d5={'name':'aatir','name':'rahul'}
print(d5)
# mutable items as keys 
d6={'name':'aatir',(1,2,3):2}
print(d6)

