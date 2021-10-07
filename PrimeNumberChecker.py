def prime_checker(number):
  is_prime = True
  for new in range(2,number):
    if number % new == 0:
      is_prime = False 
    if is_prime:
      print('It is a prime')
    else:
      print('It is not a prime')  
prime_checker(8)
