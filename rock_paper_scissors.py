import random

player_wins = 0
computer_wins = 0

options = ["rock", "paper", "scissors"]


while True:
    player_input = input("Enter (Rock / Paper/ Scissor) or E to exit: ").lower()

    #exiting the programme if option is selected
    if player_input == "e":
        break

    #Repeats the programme until user quits
    if player_input not in options :
        print("Invalid.. Type Rock, Paper or Scissors.. or E to just quit.. dont be dumb")
        continue
    random_num = random.randint(0,2)
    # setting the computer input using index of the options list
    # rock =0, paper = 1, scissors =2
    computer_guess = options[random_num]
    print("Glorious Computer picked",computer_guess + ".")

    # Setting the winning conditions according to user inputs
    if player_input == "rock" and computer_guess == "scissors":
        print("Great You won!!.. You won a candy Bar")
        player_wins += 1


    elif player_input == "paper" and computer_guess == "rock":
        print("Great You won!!.. You won a candy Bar")
        player_wins += 1


    elif player_input == "scissor" and computer_guess == "paper":
        print("Great You won!!.. You won a candy Bar")
        player_wins += 1

    else:
        print("You lost!!!.. Your Laptop won.. great..")
        computer_wins += 1


#printing end game texts
print("You won", player_wins,"times")
print("Computer won", computer_wins, "times")
print("Farewell.. Traveller")
