alphabets = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
direction = input("Type 'encode' for encoding, 'decode' for decoding:")
user_message = input('Your message here: ').lower()
shift = int(input('Number of positions to shift: '))

def encrypt(plain_text, shift_amount):
  cipher_text = ""
  for letter in plain_text:
    position = alphabets.index(letter)
    new_position = position + shift_amount
    cipher_text += alphabets[new_position]
  print(f"The encoded text is {cipher_text}")

def decrypt(cipher_text, shift_amount):
  plain_text = ""
  for letter in cipher_text:
    position = alphabets.index(letter)
    new_position = position - shift_amount
    plain_text += alphabets[new_position]
  print(f"The decoded text is {plain_text}")

if direction == 'encode':
  encrypt(plain_text=user_message,shift_amount = shift)  
if direction == 'decode':
  decrypt(cipher_text==user_message,shift_amount = shift) 
