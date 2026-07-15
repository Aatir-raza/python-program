class atm:
  # constructor (special funcn superpower)
  def __init__(self):
    self.pin=''
    self.balance=0
    print('mai to execute ho gya')

  def menu(self):
    user_input=input("""hi how can i help you 
    1.press 1 to create pin
    2.press to change pin
    3.press 3 to check balance
    4.press 4 to withdraw""")

    if user_input=='1':
     # create pin
        self.create_pin()

    elif user_input=='2':
  # change pin 
      self.change_pin()


    elif user_input=='3':
      self.checkbalance()

  
    elif user_input=='4':
      self.withdraw()

    else:
      exit()

  def create_pin(self):
    user_pin=input('enter your pin')
    self.pin=user_pin
    user_balance=int(input('enter balance'))
    self.balance=user_balance
    print('pin created successfully')
    self.menu()

  def change_pin(self):
    old_pin=input('enter old pin')

    if old_pin==self.pin:
      #let him change the pin
      new_pin=input('enter')
      self.pin=new_pin
      print('pin change successfully')
      self.menu()

    else:
      print('nai karne de skta re baba')
      self.menu()


  def checkbalance(self):
    user_pin =input('enter your pin')
    if user_pin==self.pin:
      print('your balance is',self.balance)

    else:
      print('chal nikal yahan se')

  
  def withdraw(self):
    user_pin=input('enter the pin')
  
    if user_pin==self.pin:
      #allow to withdraw
      amount=int(input('enter the amount'))

      if amount<=self.balance:
        self.balance=self.balance-amount
        print('withdraw succesful.balance is',self.balance)


      else:
        print('abe gareeb')

    else:
      print('chor')
      self.menu()
          
object=atm()
object.menu()