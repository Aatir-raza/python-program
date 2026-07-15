my_dict={'name':'jack','age':26}
# []
print(my_dict['age'])
# get
my_dict.get('age')
# adding key_value pair
d4=dict([(1,1),(2,2),(3,3)])
print(d4)
d4['gender']='male'
print(d4)
d4['weight']=72
print(d4)
# remove key value pair 
d={'name':'nitish','age':32,3:3,'gender':'male','weight':72}
# pop
d.pop('age')
print(d)
# pop item
d.popitem()
print(d)
# del
del d['name']
print(d)
# clear
d.clear()
print(d)


