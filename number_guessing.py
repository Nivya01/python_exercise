
import random
import sys
print('\n\n')
guess = int(input('Guess the number from 1 to 10:'))
if guess <1 or guess>10:
    sys.exit("You entered invalid number")
computer = random.randint(1,10)
print("Computer chose number: ",computer)
if guess == computer:
    print("yeah hoo,Your guess is correct",'\n')
else:
    print("oh no,Your guess is wrong",'\n')

