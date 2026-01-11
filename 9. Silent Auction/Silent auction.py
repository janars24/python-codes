import os
from linecache import clearcache


def find_highest_bidder(bidding_dictionary):
    winner = max(bidding_dictionary, key=bidding_dictionary.get)
    highest_bid = bidding_dictionary[winner]

    max(bidding_dictionary)
    print(f"The winner is {winner} with a bid of {highest_bid}")

bids = {}
continue_bidding = True
while continue_bidding:
    name = input("What is your name?: ")
    price = int(input("Enter your auction price: "))
    bids[name] = price
    should_continue = input("Are there other bidders | 'Yes' or 'No': "). lower()
    if should_continue == "no":
        continue_bidding = False
        find_highest_bidder(bids)
    else:
        print("\n" * 20)





