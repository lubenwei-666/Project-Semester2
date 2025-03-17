 # Guess a random number
 # Author: Zhang Junhao
 # DATE: 25/3/17

import random
a = random.randint(10,20)
guess = 0
while (guess != a):
    guess = int (input("please enter a number between 10 and 20:"))
print("congratulation！")   
