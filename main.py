from replit import clear
#HINT: You can call clear() to clear the output in the console.

from art import logo
print(logo)

user_name = input('What is your name?')
bid_amount = int(input('How much will you bid.\n$'))
# while confirm == 'yes':
bid_log = []
def bid_checker(name,amount):
    bid_dict = {}
    bid_dict[name] = amount
    bid_log.append(bid_dict)

bid_checker(name = user_name, amount = bid_amount)

confirm = input('are there any more bidders. yes or no.\n').lower()
while confirm == 'yes':
    clear()
    user_name = input('What is your name?')
    bid_amount = int(input('How much will you bid.\n$'))
    bid_checker(name = user_name, amount = bid_amount)
    
    confirm = input('are there any more bidders. yes or no.\n').lower()
    
# print(bid_log)
highest = 0
winner = ''
for pair in bid_log:
    for key in pair:
        if (pair[key]) > highest:
            highest = pair[key]
            winner = key

print(f'The winner of the auction was {winner} with a bid of {highest}')