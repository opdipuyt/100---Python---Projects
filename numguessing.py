import random
import math

lower = int(input("Enter the lower bound : "))
upper = int(input("Enter the upper bound  : "))

x= random.randint(lower,upper)
total_chance = math.ceil(math.log(upper - lower + 1,2))
print("\n\tYou've only ",total_chance, "chance to guess the integer\n")

count =0
flag = False
while count < total_chance:
    count += 1
    guess = int(input("your guess number is:"))
    if x ==guess:
        print("Congratulations you did it in ",count,"try")
        flag = True
        break
    elif x > guess:
        print("you guessed too small")
    elif x< guess:
        print("you guessed too high")
if not flag:
    print("\nThe number is %d"% x)
    print("\tBetter luck Next time")