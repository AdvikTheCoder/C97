import random
print('Number Guesiing Game')
number=random.randint(1,9)
chances=0
print('Guess a number (between 1 and 9):')

while chances<5:
  guess= int(input('Enter Your Guess:-'))
  if guess ==number:
      print('Congratulation You Won')

  elif guess<number:
          print('Your Guess Was Too Low:Guess a number higher than',guess)
  else:
       print('Your guess was too high:Guess a number lower than',guess)



if not chances<5:
    print('YOU LOSE !! ,The number is',number)


