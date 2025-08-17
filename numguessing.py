# mini number guessing and easy projects

import random
lowest_num = 10
highest_num = 100
answer = random.randint(lowest_num, highest_num)
guesses = 0
is_running  = True
print("Python Number guessing game")
print(f"Select a number between {lowest_num} and  {highest_num}")

while is_running:
    guess = input("Enter your guess : ")
    if guess.isdigit():
        guess = int(guess)
        guesses += 1
        if guess < lowest_num or guess > highest_num:
            print("that number is out of range")
            print(f"Please Select a number between {lowest_num} and  {highest_num}")
        elif guess < answer:
            print("Too low ! Try again ")
        elif guess > answer:
            print("Too high Try again ")
        else:
            print("********************************")
            print(f"Correct the answer was :{answer}")
            print(f"Number of guess {guesses}")
            print("********************************")
            is_running = False

    else:
        print("Invalid guess")
        print(f"Please select  a number between {lowest_num} and  {highest_num}")



# Number guessing game and hard project 2

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
    elif x < guess:
        print("you guessed too high")
if not flag:
    print("\nThe number is %d"% x)
    print("\tBetter luck Next time")