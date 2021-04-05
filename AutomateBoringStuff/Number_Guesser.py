import random

name = input('Enter your name:')
print('Hi!' + name + ', guess an number from 1 to 20')

number = random.randint(1, 20)

for num in range(1, 7):
    guessed_number = int(input())
    if guessed_number > number:
        print('A little less to that')
    elif guessed_number < number:
        print('A little higher')
    else:
        break

if guessed_number == number:
    print(f'Yay! That is a correct guess in {num} tries')
else:
    print(f'Nope!, My guess is {number}')
