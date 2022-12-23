import random

def player_is_winner(comp_choice, player_choice):
    if player_choice == "ROCK" and comp_choice == "SCISSORS":
        return True
    elif player_choice == "PAPER" and comp_choice == "ROCK":
        return True
    elif comp_choice == "PAPER" and player_choice == "SCISSORS":
        return True
    else:
        return False
    
def comp_is_winner(comp_choice, player_choice):
    if comp_choice == "ROCK" and player_choice == "SCISSORS":
        return True
    elif comp_choice == "PAPER" and player_choice == "ROCK":
        return True
    elif player_choice == "PAPER" and comp_choice == "SCISSORS":
        return True
    else:
        return False

def get_winner(comp_choice, player_choice):
    
    if player_is_winner(comp_choice, player_choice):
        print("Player wins this round!")
        print(f"{player_choice} wins against {comp_choice}.")   
        return True
    elif comp_is_winner(comp_choice, player_choice):
        print("Computer wins this round!")
        print(f"{comp_choice} wins against {player_choice}.")  
        return False
def check_overall_winner(comp, player):
    if comp == player:
        print("Its a draw,there is no overall winner!")
    elif comp > player:
        print("The computer is the winner!Sorry try again next time!")
    elif comp < player:
        print("The computer is the winner!Sorry try again next time!")
def run_game():   
    comp_choice = ("ROCK","PAPER","SCISSORS")
    # num_play = random.choice(range(1,6))
    num_play = 3

    num_player_wins = 0
    num_comp_wins = 0

    while num_play > 0:
        comp_play = random.choice(comp_choice)
        player_choice = input('Please enter your choice.ROCK,PAPER or SCISSORS: ').upper()
        print(comp_play)
        if comp_play == player_choice:
            print("Its a tie!")
        elif get_winner(comp_play, player_choice):
            num_player_wins += 1
        elif get_winner(comp_play, player_choice):
            num_comp_wins += 1
        # elif isinstance(get_winner(comp_play, player_choice),None):
        #     pass
        num_play -= 1
    check_overall_winner(num_comp_wins, num_player_wins)


if __name__ == "__main__":
    run_game()
    
    
    

