def add(n1,n2):
  return n1+n2

def sub(n1,n2):
  return n1-n2

def mul(n1,n2):
  return n1*n2

def div(n1,n2):
  return n1/n2  

operations = {
    '+':add,
    '-':sub,
    '*':mul,
    '/':div
}

n1 = int(input('Enter number: '))
n2 = int(input('Enter number: '))

for symbols in operations:
  print(symbols)

operation_symbol = input('Pick an operation from above: ')
calculation = operations[operation_symbol]  
answer = calculation(n1,n2)
print(f'{n1}{operation_symbol}{n2}={answer}')
