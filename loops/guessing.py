# guessing game 

#generate a random integer between 1 and 100

import random
jackpot=random.randint(1,100)
guess=int (input('guess karo'))
while guess!=jackpot:
  if guess< jackpot:
    print('galat guess higher')
  else:
    print('galat guess lower')
  guess=int(input('guess karo'))
else:
  print('correct guess')

    