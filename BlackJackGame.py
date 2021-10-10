import random

def deal_card():
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card = random.choice(cards)
  return card

def calculate_score(cards):
  # Inside calculate_score() check for a blackjack (ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.
  if sum(cards) == 21 and len(cards) == 2:
    return 0  #Blackjack

  #Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1.
  if 11 in cards and sum(cards) > 21:
    cards.remove(11)
    cards.append(1)
  return sum(cards)

#Once the user is done and no longer wants to draw more cards, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 16.
def computer_play(cards):
  score = calculate_score(cards)
  if score == 0:
    return 0
  while score < 17:
    cards.append(deal_card())  
    score = calculate_score(cards)
  return score

#Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.
def compare(user_score, computer_score):
  if user_score == computer_score:
    return "Draw 🙃"
  elif computer_score == 0:
    return "Lose, opponent has Blackjack 😱"
  elif user_score == 0:
    return "Win with a Blackjack 😎"
  elif user_score > 21:
    return "You went over. You lose 😭"
  elif computer_score > 21:
    return "Opponent went over. You win 😁"
  elif user_score > computer_score:
    return "You win 😃"
  else: 
    return "You lose 😤"

# Deal the user and computer 2 cards each using deal_card()
# def play_game():

user_cards = []
computer_cards = []
is_game_over = False

for _ in range(2):
  user_cards.append(deal_card())
  computer_cards.append(deal_card())

# The score will need to be rechecked with every new card drawn and the checks in Hint 8 need to be repeated until the game ends.
while not is_game_over:

    # Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.
  user_score = calculate_score(user_cards)
  computer_score = calculate_score(computer_cards)
  print(f"   Your cards: {user_cards}, current score: {user_score}")
  print(f"   Computer's first card: {computer_cards[0]}")

  if user_score == 0 or computer_score == 0 or user_score > 21:
    is_game_over = True
  else:      
      # If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.
    user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
    if user_should_deal == 'y':
      user_cards.append(deal_card())
    else:
      is_game_over = True

computer_score = computer_play(computer_cards)
print(f"   Your final hand: {user_cards}, final score: {user_score}")
print(f"   Computer's final hand: {computer_cards}, final score: {computer_score}")
print(f"{compare(user_score, computer_score)}")
