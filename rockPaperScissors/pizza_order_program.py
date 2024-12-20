# Based on a user's order, work out their final bill. Use the input() function to get a user's preferences and then add up the total for their order and tell them how much they have to pay.

#Small pizza (S): $15
#Medium pizza (M): $20
#Large pizza (L): $25
#Add pepperoni for small pizza (Y or N): +$2
#Add pepperoni for medium or large pizza (Y or N): +$3
#Add extra cheese for any size pizza (Y or N): +$1

print("Welcome to Python Pizza! Let's work out the bill for your order")
pizza_size_input = input("Size of your pizza? Enter small, medium or large \n").lower()
print( "size input was " + pizza_size_input)
size_cost = 25
def pizza_size_price_func(size_cost):
    if pizza_size_input == "small":
        print("ENTERED SMALL HERE")
        print("SIZE COST BEFORE CHANGE, SHOULD BE 25 " + str(size_cost))
        return 15
        #print("SIZE COST BEFORE CHANGE, SHOULD BE 15 " + str(size_cost))
    elif pizza_size_input == "medium":
         return 20
    else:
        return 25
pizza_size_price = pizza_size_price_func(size_cost) 
pepperoni_yes_or_no = input("Would you like pepperoni with that? Type yes or no \n").lower()
def pepperoni_price_function(pepperoni_yes_or_no, pizza_size_input):
    if pizza_size_input == "small":
        if pepperoni_yes_or_no == "yes":
            return 2
        else:
            return 0
    elif pizza_size_input == "medium":
         if pepperoni_yes_or_no == "yes":
            return 3
         else:
            return 0
    elif pizza_size_input == "large":
        if pepperoni_yes_or_no == "yes":
            return 4
        else:
            return 0
pepperoni_upcharge = pepperoni_price_function(pepperoni_yes_or_no, pizza_size_input)
cheese_yes_or_no = "no"
cheese_yes_or_no = input("Add cheese? Type yes or no \n ")
def cheese_price_function(cheese_yes_or_no):
    if cheese_yes_or_no == "yes":
        return 2
    else:
        return 0
cheese_upcharge = cheese_price_function(cheese_yes_or_no)
print("Pizza size cost is " + str(pizza_size_price))
print("Pepperoni upcharge " + str(pepperoni_upcharge))
print("Cheese upcharge " + str(cheese_upcharge))
pizza_price = str(int(pizza_size_price) + int(pepperoni_upcharge) + int(cheese_upcharge))
print("Your bill is " + pizza_price)
