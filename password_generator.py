import random
letter = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','x','y','z',
          'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
symbols=['!','@','#','$','%','^','&','*','(',')']
numbers = ['0','1','2','3','4','5','6','7','8','9']
print('Welcome to Random password generator!!')
nr_letter = int(input('Enter the letters you want in password:'))
nr_symbols = int(input('Enter the symbols you want in password: '))
nr_numbers = int(input('Enter the numbers you want in password: '))

password=[]

for char in range(1,nr_letter+1):
    random_char = random.choice(letter) #picks a random letter from the given sequence
    password.append(random_char)
for symbol in range(1,nr_symbols+1):
    random_sym = random.choice(symbols)
    password.append(random_sym)
for nums in range(1,nr_numbers+1): #picking the numbers required
    random_num = random.choice(numbers) # randomly picking letters from the list above
    password.append(random_num)

print(password)
random.shuffle(password) # this method shuffles data for given sequence

new_password=""
for ele in password:
    new_password += ele

print(f'Your password can be -> {new_password}')
