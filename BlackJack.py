import random
suits=['spaded','clubs','hearts','diamonds']
#value=10
cards=[]
cards_dealt=[]
ranks=['K','Q','J','A','2','3','4','5','6','7','8','9','10']
#print("Your card is: "+ rank + " of "+ suit)
#suits.append('snakes')
for suit in suits:
    for rank in ranks:
        cards.append([suit,rank])
def shuffle():
    random.shuffle(cards)
def deal(n):
    for i in range(n):
        cards_dealt.append(cards.pop())
shuffle()
deal(3)
print(cards_dealt)