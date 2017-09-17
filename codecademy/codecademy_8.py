'''
phrase = "A bird in the hand..."

# Add your for loop

for a in phrase:
  if (a == "A" or a == "a"):
    print ("X"),
  else:
    print (a),



#Don't delete this print statement!
print
'''
'''
hobby = []

for x in range(3):
  hobby.append(input("Digite um hobby: "))
  x += 1
  
print (hobby)
'''

'''
from random import randint

# Generates a number from 1 through 10 inclusive
random_number = randint(1, 10)

guesses_left = 3
# Start your game!

while (guesses_left > 0):
  guess = int(raw_input("%i - Try a number: " % guesses_left))
  
  if (guess == random_number):
    print ("You win")
    break
  
  
  guesses_left -= 1
  
else:
  print ("You Lose!")

'''
