import random
user_choice=int(input('Lets play rock paper scissor? 0 for rock, 1 for paper, 2 for scissor: '))
rock="""
                _    
               | |   
 _ __ ___   ___| | __
| '__/ _ \ / __| |/ /
| | | (_) | (__|   < 
|_|  \___/ \___|_|\_\ 
"""
paper = """
 _ __   __ _ _ __   ___ _ __ 
| '_ \ / _` | '_ \ / _ \ '__|
| |_) | (_| | |_) |  __/ |   
| .__/ \__,_| .__/ \___|_|   
| |         | |              
|_|         |_|  
"""
scissor="""
          _                        
         (_)                       
 ___  ___ _ ___ ___  ___  _ __ ___ 
/ __|/ __| / __/ __|/ _ \| '__/ __|
\__ \ (__| \__ \__ \ (_) | |  \__ \ 
|___/\___|_|___/___/\___/|_|  |___/
"""
list_data = [rock,paper,scissor]
computer_random = random.randint(0,2)
if list_data[user_choice] == list_data[computer_random]:
    print("The user choice\n"+list_data[user_choice])
    print("The computer choice\n"+list_data[computer_random])
    print('YOU WON!!!')
else:
    print("The user choice\n" + list_data[user_choice])
    print("The computer choice\n" + list_data[computer_random])
    print('YOU LOSE!!!')