logo = """
 _____________________
|  _________________  |
| | JO           0. | |
| |_________________| |
|  ___ ___ ___   ___  |
| | 7 | 8 | 9 | | + | |
| |___|___|___| |___| |
| | 4 | 5 | 6 | | - | |
| |___|___|___| |___| |
| | 1 | 2 | 3 | | x | |
| |___|___|___| |___| |
| | . | 0 | = | | / | |
| |___|___|___| |___| |
|_____________________|

"""
def add(n1,n2):
  return n1+n2

def sub(n1,n2):
  return n1-n2

def mul(n1,n2):
  return n1*n2

def div(n1,n2):
  return n1/n2  
# with return we can do more operations with the output, where as print don't give that flexibility
operations = {
    '+':add,
    '-':sub,
    '*':mul,
    '/':div
}

def calculator():
  print(logo)

  n1 = float(input('Enter number: '))

  for symbols in operations:
    print(symbols)

  should_continue = True

  while should_continue:
    operation_symbol = input('Pick an operation from above: ') 

    n2 = float(input('Enter number: '))   #second input

    calculation = operations[operation_symbol]  
    answer = calculation(n1,n2)
    print(f'{n1}{operation_symbol}{n2}={answer}')

    if input("If you wish to continue, enter 'y' :") == 'y':
      n1 = answer
    elif input("enter 'n' to start a new calculator or type 'no' to exit:") == 'n':
      should_continue = False
      calculator()
    else:
      should_continue = False  

calculator()  
