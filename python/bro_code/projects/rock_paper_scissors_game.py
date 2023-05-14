import random 

choices = ["rock", "paper", "scissors"] 
player_score = 0
computer_score = 0 


while True:
    computer = random.choice(choices)
    player = None
    while player not in choices:
        player = input("rock, paper, or scissors?: ").lower()

    print("Computer" ,computer, " ", "player", player)
    print("*****************************************")

    if player == computer:
        print("tie")
    elif player == "rock":
        if computer == "scissors":
            print("player won")
            player_score += 1
        elif computer == "paper":
            print("computer won you lose")
            computer_score += 1 
    elif player == "paper":
        if computer == "scissors":
            print("computer won you lose")
            computer_score += 1 

        elif computer == "rock":
            print("player won")
            player_score += 1        
    else:
        if computer == "rock":
            print("computer won you lose")
            computer_score += 1 

        elif computer == "paper":
            print("player won")
            player_score += 1
    
    print("computer: ", computer_score, "player: ", player_score)
    print("------------------------") 
    if computer_score == 5:
        print("computer won match ended")
        break
    elif player_score == 5:
        print("player won match ends")
        break