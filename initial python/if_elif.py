email = input('enter email ')
password = input('enter password ')

if email == 'Aatir.campusx@gmail.com' and password == '1234':
    print('welcome')

elif email == 'Aatir.campusx@gmail.com'and password !='1234':
    # tell the user
    print('incorrect password')
    password = input('enter password again ')
    
    if password == '1234':
        print('welcome finally')
    else:
        print('beta tumse na ho payega')

else:
    print('not correct')

