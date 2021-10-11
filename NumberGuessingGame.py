import random
logo = """

     ___       _______   __    ______        _______.
    /   \     |       \ |  |  /  __  \      /       |
   /  ^  \    |  .--.  ||  | |  |  |  |    |   (----`
  /  /_\  \   |  |  |  ||  | |  |  |  |     \   \    
 /  _____  \  |  '--'  ||  | |  `--'  | .----)   |   
/__/     \__\ |_______/ |__|  \______/  |_______/    
                                                     

"""
print('Welcome to number guessing game')
print('I am thinking of number between 1 to 100:')
game_type = input('Choose the difficulty. Type \'easy\' or \'hard\'')
number = random.randint(1,100)
number_of_attempts = 0
if game_type == 'easy':
  number_of_attempts = 10
elif game_type == 'hard':
  number_of_attempts = 5

for i in range(number_of_attempts):
  print('Number of attempts left',number_of_attempts-i)
  user_in = int(input("Make a guess: "))
  if number<user_in:
    print('Too high.')
  elif number>user_in:
    print('Its too low') 
  elif number == user_in:
    print("Yay! thats a correct guess")
    break   

print(logo) 
