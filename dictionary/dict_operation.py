# MEMEBRSHIP
d={'name':'nitish','age':32,3:3,'gender':'male','weight':72}
print('name'in d)
# iteration
for i in d:
  print(i,d[i])

 # dictionary fumction
# len/sorted
print(len(d))
print(sorted(d,key=str,reverse=True))
print(min(d,key=str)) 
# item/keys/values
print(d)
print(d.items())
print(d.keys())
print(d.values())
# update 
d1={1:2,3:4,4:5}
d2={4:7,6:8}
d1.update(d2)
print(d1)

