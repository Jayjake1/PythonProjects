# Conditionals, logicals, code blocks, scopes

print('Welcome to the Tresure island\nYour mission is to find tresure \n ')

start = input('You are a cross road, where do you want to go? Left or Right:').lower()

if start == 'left':
    at_river = input('Safe move!, You are at a river, Would you like to "wait" or "swim": ').lower()
    if at_river == 'wait':
        doors_input=int(input('There are 3 doors which one do you like to enter: 1, 2 ,3: '))
        if doors_input == 1:
            print('There is red wine, thats somewhat tressure')
        elif doors_input == 2:
            print('Ah! you found a ruby')
        elif doors_input == 3:
            print('You just found a box full of gold, good luck')
        else:
            print('Please enter input either 1 or 2 or 3')
    else:
        print('You were eaten by crocs, Better luck')
else:
    print('You met with accident, Better luck next time')

print('Thanks for playing')