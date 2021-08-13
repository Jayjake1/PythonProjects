# using type conversion, f string, round function, operations
# welcome greeting
print('Welcome to the tip calculator:')
# getting total bill from user
total_bill = float(input('What was the total bill? $ '))  # type convering
# tip percentage
tip_percentage = int(input('what percentage of tip would you like to give? 10, 12, 15 : '))
# How many people
people_count = int(input('Number of people: '))
# tip calculation
split_bill = total_bill/people_count
tip = (split_bill)*(tip_percentage/100)
tip_for_each = round(split_bill+tip,2 ) # to get the round of continuous output
print(f'Each person should pay: ${tip_for_each}')