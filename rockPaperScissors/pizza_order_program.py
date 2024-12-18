# Based on a user's order, work out their final bill. Use the input() function to get a user's preferences and then add up the total for their order and tell them how much they have to pay.

#Small pizza (S): $15
#Medium pizza (M): $20
#Large pizza (L): $25
#Add pepperoni for small pizza (Y or N): +$2
#Add pepperoni for medium or large pizza (Y or N): +$3
#Add extra cheese for any size pizza (Y or N): +$1

print("Welcome to Python Pizza! Let's work out the bill for your order")
pizza_size_input = input("Size of your pizza? Enter small, medium or large \n")
print( "size input was " + pizza_size_input)
size_cost = 25
def pizza_size_price_func(size_cost):
    if pizza_size_input == "small":
        print("ENTERED SMALL HERE")
        print("SIZE COST BEFORE CHANGE, SHOULD BE 25 " + str(size_cost))
        size_cost = 15
        print("SIZE COST BEFORE CHANGE, SHOULD BE 15 " + str(size_cost))
    elif pizza_size_input == "medium":
         size_cost = 20
    else:
        size_cost = 25
pizza_size_price_func(size_cost) # not calling function? or not recognizing size_cost as the same variable?
print("SIZE COST AFTER CALLING FUNCTION, SHOULD BE 15 " + str(size_cost))
pepperoni_yes_or_no = False
pepperoni_upcharge = 0
pepperoni_yes_or_no = input("Would you like pepperoni with that? Type True for yes or False for no \n")
def pepperoni_price_function():
    if pizza_size_input == "small":
        if pepperoni_yes_or_no == True:
            pepperoni_upcharge = 2
    elif pizza_size_input == "medium":
         if pepperoni_yes_or_no == True:
            pepperoni_upcharge = 3
    elif pizza_size_input == "large":
            if pepperoni_yes_or_no == True:
                pepperoni_upcharge = 4
pepperoni_price_function()
cheese_yes_or_no = False
cheese_upcharge = 0
cheese_yes_or_no = input("Add cheese? Type True for yes or False for no \n ")
def cheese_price_function():
    if cheese_yes_or_no == True:
        cheese_upcharge = 2
cheese_price_function()
print("Pizza size cost is " + str(size_cost))
print("Pepperoni upcharge " + str(pepperoni_upcharge))
print("Cheese upcharge" + str(cheese_upcharge))
pizza_price = str(int(size_cost) + int(pepperoni_upcharge) + int(cheese_upcharge))
print("Your bill is " + pizza_price)
