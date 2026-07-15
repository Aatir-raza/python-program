# print 1st 10 numbers and their squares
s={i:i**2 for i in range(1,11)}
print(s)
# USING EXISTING DICT 
distances={'delhi':1000,'mumbai':2000,'banglore':3000}
print({key:value*0.62 for (key,value) in distances.items()})
# using zip 
days=["sunday","monday","tuesday","wednesday","thrusday","friday","saturday"]
tem_c=[30.5,32.5,31.8,33.4,29.8,30.2,29.9]
print({i:j for (i,j) in zip (days,tem_c)})
# using if condition 
products={'phones':10,'laptop':0,'charger':32,'tablets':0}
print({key:value for (key,value) in products.items()if value>0})
# nested comprehension
# print tables of number from 2 to 4
print({i:{j:i*j for j in range(1,11)} for i in range(2,5)})
