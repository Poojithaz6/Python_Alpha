import random as r
#player_choice=5
#print(type(player_choice))

def get_choice():
    player_choice=input("Enter a choice:")
    opt=['rock','paper','scissor']
    computer_choice=r.choice(opt)
    dict={"player":player_choice,"Computer":computer_choice}
    return dict
def check_win():
    choice = get_choice()
    player=choice['player']
    computer=choice['Computer']
    print(f"you chose {player}, computer chose {computer}")
    if player==computer:
        return check_win()
check_win()



