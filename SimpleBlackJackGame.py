import random
print('Welcome to Black Jack✌🏼')
cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]

for i in range(3):
  comp_card = []
  comp_card.append(random.choice(cards))
# comp_card.append(comp_picking)
  user_card=[]
  if input("Your turn, enter 'y' to pick and 'n' to stop picking: ") == 'y':
    user_picking = random.choice(cards)
    user_card.append(user_picking)

comp = sum(comp_card)
user = sum(user_card)
if comp == user:
  print('Draw')
elif (comp > user) & (comp<21):
  print('computer wins')
elif (user > comp) & (user<21):
  print('User wins')     

print(sum(comp_card))
print(sum(user_card))
