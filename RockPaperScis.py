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
    elif player=='rock':
        if computer=='paper':
            return "Paper covers rock, you loose!"
        return "Rock smashes scissors, you win!"

    elif player=='paper':
        if computer=='scissor':
            return "Scissor cuts paper, you loose!"
        return "paper covers rock, you win!"

    elif player=='scissor':
        if computer=='rock':
            return "Rock smashes scissors, you loose!"
        return "Scissor cuts paper, you win!"
    else:
        return"Spelling error"
print(check_win())



