# mini project rock paper scissors

import random

option = ("rock","paper","scissors")

running = True

while running:
    player = None
    computer = random.choice(option)
    while player not in option:
        player = input("Enter a choice (rock , paper , scissors ) : ")

    print(f"player : {player}")
    print(f"computer : {computer}")

    if player == computer:
        print("It's a tie")
    elif player == "rock" and computer == "scissors":
        print("you win ")
    elif player == "paper" and computer == "rock":
        print("you win ")
    elif player == "scissors" and computer == "paper":
        print("you win ")
    else:
        print("you lose")
    play_again = input("player again (y/n) : ").lower()
    if not play_again == "y":
        running = False
# one line statements


    # if not input("play again ? (y/n) :").lower() == "y":
    #     break
print("thanks for playing ")



