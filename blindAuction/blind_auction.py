bids = {"Valeria": "900", "Anna": "100", "Jim": "300"}
def enter_bids_and_add_to_dictionary(dictionary):
    user_name = input("What is your name? \n")
    user_bid = int(input("What is your bid? \n"))
    dictionary[user_name] = user_bid
def ask_for_bids():
    enter_bids_and_add_to_dictionary(bids)
    continue_bidding = input("any more bidders -  yes or no \n")
    if continue_bidding == "yes":
        ask_for_bids()
def compare_bids():
    highest_bid = 0
    for key in bids:
        #print(bids[key])
        current_bid = int(bids[key]) 
        current_bidder = key
        print("current bid ", current_bid)
        print("highest bid ", highest_bid)
        if current_bid > highest_bid:
            highest_bid = current_bid
            highest_bidder = current_bidder
    print(highest_bid)
    print("higest bidder wins: ", highest_bidder)
    return highest_bid  
def blind_auction_game():
    ask_for_bids()
    compare_bids()
blind_auction_game()