logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
print(logo)
auction_dict = {}
bidding_finished=False

def highest_bidder(auction_dict):
  highest_bid = 0
  winner = ""
  for key in auction_dict:
    current_bid = auction_dict[key]
    if current_bid>highest_bid:
      highest_bid=current_bid
      winner = key
  print('The winner is ',winner)  
  
while not bidding_finished:
  bidder_name = input('Enter your name here : ')
  bid_price = int(input('Your bid: $'))
  auction_dict[bidder_name] = bid_price
  re_bid=input('Any other bids, if yes type in \'yes\' or type no: ').lower()
  if re_bid=='no':
    bidding_finished=True
    highest_bidder(auction_dict)
  elif re_bid=='yes':
    bidding_finished = False  
