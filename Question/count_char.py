#COUNT THE FREQUENCY OF A PARTICULAR CHARACTER IN A PROVIDED STRING 
# Eg "HELLOHOW ARE YOU ".IS THE STRING THE FREQUENCY OF H IN THIS STRING IN 2

s=input('enter the email')
term=input('what would like to search for')

counter=0
for i in s:
  if i == term:
    counter+=1
print('frequency',counter)    
